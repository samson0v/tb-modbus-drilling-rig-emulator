from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_MUD_TEMPERATURE, PREVENTER_MUD_TEMPERATURE_MAX, PREVENTER_MUD_TEMPERATURE_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudTemperatureSensor(Sensor):
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

        self.__temperature = self.generate_value(self.__temperature, 2, PREVENTER_MUD_TEMPERATURE_MIN, PREVENTER_MUD_TEMPERATURE_MAX)

    def set_init_value(self):
        self.__temperature = PREVENTER_MUD_TEMPERATURE

    def cooling(self):
        if self.__temperature > 0:
            self.__temperature -= 1
