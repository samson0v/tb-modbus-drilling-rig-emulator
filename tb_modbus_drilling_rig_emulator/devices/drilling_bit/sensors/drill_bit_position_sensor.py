from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class DrillBitPositionSensor(Sensor):
    def __init__(self, address, position):
        super().__init__(address)
        self.__position = position

    @property
    def position(self):
        return self.__position

    def reset(self):
        self.__position = 0

    def update(self, speed):
        self.__position += speed
