from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRAWWORK_VIBRATION_MAX, DRAWWORK_VIBRATION_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class VibrationSensor(Sensor):
    def __init__(self, address, vibration_level):
        super().__init__(address)
        self.__vibration_level = vibration_level

    @property
    def vibration_level(self):
        return self.__vibration_level

    def update(self, vibration_level=None):
        if vibration_level is not None:
            self.__vibration_level = vibration_level

        self.__vibration_level = self.generate_value(self.__vibration_level, 2, DRAWWORK_VIBRATION_MIN, DRAWWORK_VIBRATION_MAX)
