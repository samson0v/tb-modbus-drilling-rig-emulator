from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_EQUIPMENT_TEMPERATURE, PREVENTER_EQUIPMENT_TEMPERATURE_MAX, PREVENTER_EQUIPMENT_TEMPERATURE_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class EquipmentTemperatureSensor(Sensor):
    def __init__(self, address, temperature):
        super().__init__(address)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def update(self, temperature=None):
        if temperature is not None:
            self.__temperature = temperature
            return

        self.__temperature = self.generate_value(self.__temperature, 1, PREVENTER_EQUIPMENT_TEMPERATURE_MIN, PREVENTER_EQUIPMENT_TEMPERATURE_MAX)

    def set_init_value(self):
        self.__temperature = PREVENTER_EQUIPMENT_TEMPERATURE
