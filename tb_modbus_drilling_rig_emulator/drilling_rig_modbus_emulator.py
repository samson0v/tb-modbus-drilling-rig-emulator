import logging
import asyncio
import time

from pymodbus.datastore import ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server.async_io import StartAsyncTcpServer

from tb_modbus_drilling_rig_emulator.devices.drawwork.drawwork import Drawwork
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.drilling_bit import DrillingBit
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.drilling_mud import DrillingMud
from tb_modbus_drilling_rig_emulator.devices.drilling_rig.drilling_rig import DrillingRig
from tb_modbus_drilling_rig_emulator.devices.preventer.preventer import Preventer


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DrillingRigEmulator:
    def __init__(self, drilling_depth, drilling_speed, monitoring_interval):
        self.__log = logging.getLogger('DrillingRigEmulator')

        self.__identity = self.__setup_identity()

        self._running = True

        self.__monitoring_interval = monitoring_interval
        self.__drilling_depth = drilling_depth

        self.__last_monitoring_time = 0
        self.__has_reached_drilling_depth = False
        self.__emergency_stop = False
        self.__continued_drilling = False

        self.__drilling_mud_device = DrillingMud()
        self.__drilling_rig_device = DrillingRig()
        self.__drilling_bit_device = DrillingBit(self.__drilling_depth, drilling_speed)
        self.__preventer_device = Preventer()
        self.__drawwork_device = Drawwork()

        self.__device_context = self.__setup_device_context()

    @staticmethod
    def __setup_identity():
        identity = ModbusDeviceIdentification()
        identity.VendorName = 'ThingsBoard'
        identity.ProductCode = 'DrillingRigEmulator'
        identity.VendorUrl = 'https://thingsboard.io/'
        identity.ProductName = 'Drilling Rig Emulator'
        identity.ModelName = 'Modbus TCP Emulator'
        identity.MajorMinorRevision = '1.0'

        return identity

    def __setup_device_context(self):
        return {
            5035: ModbusServerContext(slaves={1: self.__drilling_bit_device.storage}, single=False),
            5036: ModbusServerContext(slaves={2: self.__drilling_mud_device.storage}, single=False),
            5037: ModbusServerContext(slaves={3: self.__drilling_rig_device.storage}, single=False),
            5038: ModbusServerContext(slaves={4: self.__preventer_device.storage}, single=False),
            5039: ModbusServerContext(slaves={5: self.__drawwork_device.storage}, single=False)
        }

    async def run(self):
        await self.__start_drilling()
        await asyncio.gather(self.__start_modbus_servers(), self.__monitor_values())

    async def __start_drilling(self):
        self.__drilling_bit_device.on()
        self.__drilling_mud_device.on()
        self.__drawwork_device.on()
        self.__preventer_device.off()
        self.__drilling_rig_device.on()

    async def __continue_drilling(self):
        self.__drilling_bit_device.on(with_init_values=False)
        self.__drilling_mud_device.on(with_init_values=False)
        self.__drawwork_device.on()
        self.__preventer_device.off(with_init_values=False)
        self.__drilling_rig_device.on(with_init_values=False)

    async def __start_modbus_servers(self):
        server_tasks = [self.__start_server(port, context) for port, context in self.__device_context.items()]
        await asyncio.gather(*server_tasks)

    async def __start_server(self, port, context):
        self.__log.info(f"Starting Modbus server on port {port}")
        await StartAsyncTcpServer(context=context, identity=self.__identity, address=("0.0.0.0", port))

    def __stop_drilling(self, emergency_stop=False):
        if emergency_stop:
            self.__preventer_device.on()
        else:
            self.__preventer_device.off()

        self.__drilling_mud_device.off()
        self.__drawwork_device.off()
        self.__drilling_bit_device.off()
        self.__drilling_rig_device.off()

        self.__log.info("Drilling rig has stopped.")

    async def __monitor_values(self):
        try:
            while self._running:
                if self.__last_monitoring_time + self.__monitoring_interval < int(time.time()):
                    self.__drilling_mud_device.update()
                    is_drilling_fluid_supplied = self.__drilling_mud_device.status and self.__drilling_mud_device.valve

                    self.__drilling_bit_device.update(is_drilling_fluid_supplied=is_drilling_fluid_supplied,
                                                      drawwork_direction=self.__drawwork_device.direction,
                                                      is_drawwork_on=self.__drawwork_device.status)
                    self.__drawwork_device.update(self.__drilling_bit_device.current_depth)
                    self.__drilling_rig_device.update(is_drilling_fluid_supplied=is_drilling_fluid_supplied)

                    if not self.__has_reached_drilling_depth:
                        self.__preventer_device.update(mud_temperature=self.__drilling_mud_device.temperature,
                                                       is_drilling_fluid_supplied=is_drilling_fluid_supplied)

                    self.__log_values()
                    await self.__check_conditions()

                    self.__last_monitoring_time = time.time()
                else:
                    await asyncio.sleep(1)
        except ValueError as e:
            self.__log.error(f"Error: {e}")
            self.__stop_drilling()

    async def __check_conditions(self):
        if self.__preventer_device.status and not self.__emergency_stop and self.__continued_drilling:
            self.__continued_drilling = False
            self.__stop_drilling(emergency_stop=True)

        if not self.__emergency_stop and not self.__preventer_device.status and not self.__continued_drilling:
            self.__continued_drilling = True
            await self.__continue_drilling()

        if self.__drilling_bit_device.temperature <= 149 and self.__preventer_device.pressure <= 29 and self.__emergency_stop:
            await self.__continue_drilling()
            self.__emergency_stop = False

        if self.__preventer_device.pressure >= 50 or self.__drilling_bit_device.temperature >= 200 and not self.__emergency_stop:
            self.__log.info("Preventer pressure is too high. Stopping the drilling process.")
            self.__emergency_stop = True
            self.__stop_drilling(emergency_stop=True)

        if self.__drilling_bit_device.current_depth >= self.__drilling_bit_device.well_depth and not self.__has_reached_drilling_depth:
            self.__log.info("Drilling rig has reached the drilling depth. Stopping the drilling process.")
            self.__has_reached_drilling_depth = True
            self.__stop_drilling()

        if self.__drilling_bit_device.current_depth < self.__drilling_bit_device.well_depth and self.__has_reached_drilling_depth:
            await self.__start_drilling()
            self.__has_reached_drilling_depth = False

        if self.__drilling_rig_device.is_running():
            if not self.__drilling_bit_device.is_running():
                self.__drilling_bit_device.on()
        else:
            if self.__drilling_bit_device.is_running():
                self.__drilling_bit_device.off()

    def __log_values(self):
        self.__log.info(self.__drilling_bit_device)
        self.__log.info(self.__drilling_mud_device)
        self.__log.info(self.__drilling_rig_device)
        self.__log.info(self.__preventer_device)
        self.__log.info(self.__drawwork_device)
        self.__log.info('----------------------------------')


if __name__ == '__main__':
    drilling_rig_emulator = DrillingRigEmulator(drilling_depth=2000, drilling_speed=35, monitoring_interval=2)
    try:
        asyncio.run(drilling_rig_emulator.run())
    except KeyboardInterrupt:
        pass
