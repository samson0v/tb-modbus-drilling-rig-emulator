from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_LEAK_LEVEL, PREVENTER_LEAK_LEVEL_MAX, PREVENTER_LEAK_LEVEL_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class SystemLeakDetectionSensor(Sensor):
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

        self.__level = self.generate_value(self.__level, 1, PREVENTER_LEAK_LEVEL_MIN, PREVENTER_LEAK_LEVEL_MAX)

    def set_init_value(self):
        self.__level = PREVENTER_LEAK_LEVEL
