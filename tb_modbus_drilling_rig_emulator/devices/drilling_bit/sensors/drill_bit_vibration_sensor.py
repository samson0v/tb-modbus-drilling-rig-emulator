from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_BIT_VIBRATION_LEVEL
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class DrillBitVibrationSensor(Sensor):
    def __init__(self, address, vibration_level):
        super().__init__(address)
        self.__vibration_level = vibration_level

    @property
    def vibration_level(self):
        return self.__vibration_level

    def update(self, vibration_level=None):
        if vibration_level is not None:
            self.__vibration_level = vibration_level
            return

        self.__vibration_level = int(self.__vibration_level + uniform(-2, 2))

    def set_init_value(self):
        self.__vibration_level = DRILLING_BIT_VIBRATION_LEVEL
