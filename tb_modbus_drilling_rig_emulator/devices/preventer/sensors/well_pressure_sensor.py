from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_PRESSURE
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

        self.__pressure = int(self.__pressure + uniform(-4, 4))

    def set_init_value(self):
        self.__pressure = PREVENTER_PRESSURE
