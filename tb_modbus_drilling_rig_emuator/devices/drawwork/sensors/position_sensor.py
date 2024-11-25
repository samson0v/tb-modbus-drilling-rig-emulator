from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class PositionSensor(Sensor):
    def __init__(self, address, position):
        super().__init__(address)
        self.__position = position

    @property
    def position(self):
        return self.__position

    def update(self, position):
        self.__position = position
