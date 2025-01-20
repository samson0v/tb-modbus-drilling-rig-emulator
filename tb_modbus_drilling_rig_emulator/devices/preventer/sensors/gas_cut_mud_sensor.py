from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_LEVEL
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class GasCutMudSensor(Sensor):
    def __init__(self, address, level):
        super().__init__(address)
        self.__level = level

    @property
    def level(self):
        return self.__level

    def update(self, level=None):
        if level is not None:
            self.__level = level
            return

        self.__level = int(self.__level + uniform(-1, 1))

    def set_init_value(self):
        self.__level = PREVENTER_LEVEL
