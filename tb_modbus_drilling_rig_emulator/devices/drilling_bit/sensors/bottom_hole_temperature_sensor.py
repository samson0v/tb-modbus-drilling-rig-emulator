from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_BIT_TEMPERATURE, DRILLING_BIT_TEMPERATURE_MAX, DRILLING_BIT_TEMPERATURE_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class BottomHoleTemperatureSensor(Sensor):
    def __init__(self, address, temperature):
        super().__init__(address)
        self.temperature = temperature

    def update(self, is_drilling_fluid_supplied):
        if self.temperature >= 200 and not is_drilling_fluid_supplied:
            raise ValueError("Drilling bit temperature is too high")

        if is_drilling_fluid_supplied and self.temperature <= 140:
            self.__increase_temperature(1)
        elif is_drilling_fluid_supplied and self.temperature > 148:
            self.__decrease_temperature(1)
        elif is_drilling_fluid_supplied and 140 <= self.temperature <= 148:
            self.temperature = self.generate_value(self.temperature, 3, DRILLING_BIT_TEMPERATURE_MIN, DRILLING_BIT_TEMPERATURE_MAX)
        elif not is_drilling_fluid_supplied:
            self.__increase_temperature(10)

    def __increase_temperature(self, value):
        self.temperature += value

    def __decrease_temperature(self, value):
        self.temperature -= value

    def set_init_value(self):
        self.temperature = DRILLING_BIT_TEMPERATURE

    def cooling(self):
        if self.temperature >= 0:
            self.temperature -= 1
