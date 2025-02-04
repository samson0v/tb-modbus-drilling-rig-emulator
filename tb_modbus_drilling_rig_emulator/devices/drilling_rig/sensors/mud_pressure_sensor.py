from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_RIG_MUD_PRESSURE
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudPressureSensor(Sensor):
    def __init__(self, address, pressure):
        super().__init__(address)
        self.__pressure = pressure

    @property
    def pressure(self):
        return self.__pressure

    def set_init_value(self):
        self.__pressure = DRILLING_RIG_MUD_PRESSURE

    def update(self, pressure=None):
        if pressure is not None:
            self.__pressure = pressure
            return

        self.__pressure = self.generate_value(self.__pressure, 2, 0, 100)
