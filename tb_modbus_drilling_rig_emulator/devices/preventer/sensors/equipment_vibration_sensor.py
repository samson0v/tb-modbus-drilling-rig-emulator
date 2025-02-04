from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_EQUIPMENT_TEMPERATURE, PREVENTER_EQUIPMENT_TEMPERATURE_MAX, PREVENTER_EQUIPMENT_TEMPERATURE_MIN
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

        self.__vibration = self.generate_value(self.__vibration, 1, PREVENTER_EQUIPMENT_TEMPERATURE_MIN, PREVENTER_EQUIPMENT_TEMPERATURE_MAX)

    def set_init_value(self):
        self.__vibration = PREVENTER_EQUIPMENT_TEMPERATURE
