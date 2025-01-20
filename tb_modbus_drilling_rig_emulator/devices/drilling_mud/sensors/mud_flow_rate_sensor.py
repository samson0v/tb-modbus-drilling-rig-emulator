from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_SPEED
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudFlowRateSensor(Sensor):
    def __init__(self, address, speed):
        super().__init__(address)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def update(self, speed=None):
        if speed is not None:
            self.__speed = speed
            return

        self.__speed = int(self.__speed + uniform(-2, 2))

    def set_init_value(self):
        self.__speed = DRILLING_MUD_SPEED
