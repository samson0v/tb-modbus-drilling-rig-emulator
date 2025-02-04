from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor
from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_RIG_RORATY_SPEED


class RotarySpeedSensor(Sensor):
    def __init__(self, address, speed):
        super().__init__(address)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def set_init_value(self):
        self.__speed = DRILLING_RIG_RORATY_SPEED

    def update(self, speed=None):
        if speed is not None:
            self.__speed = speed
            return

        self.__speed = self.generate_value(self.__speed, 1, 0, 100)
