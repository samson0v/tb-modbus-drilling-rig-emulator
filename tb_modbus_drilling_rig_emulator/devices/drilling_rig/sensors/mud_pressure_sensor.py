from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_RIG_MUD_PRESSURE, DRILLING_RIG_MUD_PRESSURE_MAX, DRILLING_RIG_MUD_PRESSURE_MIN
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

    def update(self, pressure=None, is_drilling_fluid_supplied=True):
        if not is_drilling_fluid_supplied:
            self.__pressure = 0
            return

        if pressure is not None:
            self.__pressure = pressure
            return

        self.__pressure = self.generate_value(self.__pressure, 2, DRILLING_RIG_MUD_PRESSURE_MIN, DRILLING_RIG_MUD_PRESSURE_MAX)
