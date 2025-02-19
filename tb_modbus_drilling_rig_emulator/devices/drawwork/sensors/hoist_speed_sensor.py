from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class HoistSpeedSensor(Sensor):
    def __init__(self, address, speed):
        super().__init__(address)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def update(self, speed=None):
        if speed:
            self.__speed = speed
            return

        if self.__speed <= 5:
            self.__speed = self.generate_value(self.__speed, 1, 3, 4)

        if self.__speed <= 15:
            self.__speed = self.generate_value(self.__speed, 1, 11, 14)
