from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_RIG_DRILLING_LINE_HOIST_SPEED
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class DrillingLineHoistSpeedSensor(Sensor):
    def __init__(self, address, speed):
        super().__init__(address)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def set_init_value(self):
        self.__speed = DRILLING_RIG_DRILLING_LINE_HOIST_SPEED

    def update(self, speed):
        if speed is not None:
            self.__speed = speed
            return

        self.__speed = DRILLING_RIG_DRILLING_LINE_HOIST_SPEED
