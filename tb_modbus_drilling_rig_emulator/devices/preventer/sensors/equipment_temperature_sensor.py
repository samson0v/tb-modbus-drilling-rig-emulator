from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_EQUIPMENT_TEMPERATURE
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

        self.__temperature = int(self.__temperature + uniform(-1, 1))

    def set_init_value(self):
        self.__temperature = PREVENTER_EQUIPMENT_TEMPERATURE
