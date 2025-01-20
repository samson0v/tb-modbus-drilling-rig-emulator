from tb_modbus_drilling_rig_emulator.devices.device import Device
from tb_modbus_drilling_rig_emulator.devices.drilling_rig.sensors.drilling_line_hoist_speed_sensor import \
    DrillingLineHoistSpeedSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_rig.sensors.hook_load_sensor import HookLoadSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_rig.sensors.mud_pressure_sensor import MudPressureSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_rig.sensors.rotary_speed_sensor import RotarySpeedSensor


class DrillingRig(Device):
    def __init__(self):
        super().__init__()
        self.__drilling_line_hoist_speed_sensor = DrillingLineHoistSpeedSensor(address=1, speed=0)
        self.__hook_load_sensor = HookLoadSensor(address=2, load=0)
        self.__rotary_speed_sensor = RotarySpeedSensor(address=3, speed=0)
        self.__mud_pressure_sensor = MudPressureSensor(address=4, pressure=0)

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"DrillingRig(drilling_line_hoist_speed={self.__drilling_line_hoist_speed_sensor.speed}, hook_load={self.__hook_load_sensor.load}, " \
               f"rotary_speed={self.__rotary_speed_sensor.speed}, mud_pressure={self.__mud_pressure_sensor.pressure})"

    @property
    def status(self):
        return self._running

    @property
    def drilling_line_hoist_speed(self):
        return self.__drilling_line_hoist_speed_sensor.speed

    @property
    def hook_load(self):
        return self.__hook_load_sensor.load

    @property
    def rotary_speed(self):
        return self.__rotary_speed_sensor.speed

    @property
    def mud_pressure(self):
        return self.__mud_pressure_sensor.pressure

    def on(self):
        super().on()

        self.__hook_load_sensor.set_init_value()
        self.__mud_pressure_sensor.set_init_value()
        self.__rotary_speed_sensor.set_init_value()
        self.__drilling_line_hoist_speed_sensor.set_init_value()

    def off(self):
        super().off()

        self.__hook_load_sensor.update(load=0)
        self.__mud_pressure_sensor.update(pressure=0)
        self.__rotary_speed_sensor.update(speed=0)
        self.__drilling_line_hoist_speed_sensor.update(speed=0)

        self._update_storage(6, self.get_all_sensors_values())

    def get_all_sensors_values(self) -> dict:
        return {
            self.__drilling_line_hoist_speed_sensor.address: self.__drilling_line_hoist_speed_sensor.speed,
            self.__hook_load_sensor.address: self.__hook_load_sensor.load,
            self.__rotary_speed_sensor.address: self.__rotary_speed_sensor.speed,
            self.__mud_pressure_sensor.address: self.__mud_pressure_sensor.pressure
        }

    def update(self):
        self.update_state()

        if self._running:
            self.__hook_load_sensor.update()
            self.__mud_pressure_sensor.update()
            self.__rotary_speed_sensor.update()
            self._update_storage(6, self.get_all_sensors_values())
