from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_PRESSURE, PREVENTER_PRESSURE_MAX, PREVENTER_PRESSURE_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class WellPressureSensor(Sensor):
    def __init__(self, address, pressure):
        super().__init__(address)
        self.__pressure = pressure

    @property
    def pressure(self):
        return self.__pressure

    def update(self, pressure=None):
        if pressure is not None:
            self.__pressure = pressure
            return

        self.__pressure = self.generate_value(self.__pressure, 4, PREVENTER_PRESSURE_MIN, PREVENTER_PRESSURE_MAX)

    def set_init_value(self):
        self.__pressure = PREVENTER_PRESSURE
