from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_MAX_LEVEL, DRILLING_MUD_MIN_LEVEL
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudLevelSensor(Sensor):
    def __init__(self, address, tank_capacity):
        super().__init__(address)
        self.__tank_capacity = tank_capacity
        self.__level = self.__tank_capacity / 2

    @property
    def level(self):
        return int(self.__level)

    def __as_percentage(self, value):
        return int(value / self.__tank_capacity * 100)

    def update(self):
        level = round(self.__level + uniform(-20, 20), 2)

        if DRILLING_MUD_MAX_LEVEL > self.__as_percentage(self.__level) > DRILLING_MUD_MIN_LEVEL:
            self.__level = level
