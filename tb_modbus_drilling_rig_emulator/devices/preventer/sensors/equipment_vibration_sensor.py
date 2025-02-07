from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_VIBRATION_LEVEL, PREVENTER_VIBRATION_LEVEL_MAX, PREVENTER_VIBRATION_LEVEL_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class EquipmentVibrationSensor(Sensor):
    def __init__(self, address, vibration):
        super().__init__(address)
        self.__vibration = vibration

    @property
    def vibration(self):
        return self.__vibration

    def update(self, vibration=None):
        if vibration is not None:
            self.__vibration = vibration
            return

        self.__vibration = self.generate_value(self.__vibration, 1, PREVENTER_VIBRATION_LEVEL_MIN, PREVENTER_VIBRATION_LEVEL_MAX)

    def set_init_value(self):
        self.__vibration = PREVENTER_VIBRATION_LEVEL
