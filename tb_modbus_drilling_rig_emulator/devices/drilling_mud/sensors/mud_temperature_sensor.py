from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_TEMPERATURE, DRILLING_MUD_TEMPERATURE_MAX, DRILLING_MUD_TEMPERATURE_MIN
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

        self.__temperature = self.generate_value(self.__temperature, 2, DRILLING_MUD_TEMPERATURE_MIN, DRILLING_MUD_TEMPERATURE_MAX)

    def set_init_value(self):
        self.__temperature = DRILLING_MUD_TEMPERATURE
