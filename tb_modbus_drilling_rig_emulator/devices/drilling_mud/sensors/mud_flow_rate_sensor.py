from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_SPEED, DRILLING_MUD_SPEED_MAX, DRILLING_MUD_SPEED_MIN
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

        self.__speed = self.generate_value(self.__speed, 2, DRILLING_MUD_SPEED_MIN, DRILLING_MUD_SPEED_MAX)

    def set_init_value(self):
        self.__speed = DRILLING_MUD_SPEED
