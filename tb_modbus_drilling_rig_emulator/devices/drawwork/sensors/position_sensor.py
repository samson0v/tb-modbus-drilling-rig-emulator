from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class PositionSensor(Sensor):
    def __init__(self, address, position):
        super().__init__(address)
        self.__position = position

    @property
    def position(self):
        return self.__position

    def update(self, position, direction, speed):
        if not direction:
            self.__position = position
        else:
            if self.__position >= 0:
                self.__position = self.__position - speed

            if self.__position < 0:
                self.__position = 0
