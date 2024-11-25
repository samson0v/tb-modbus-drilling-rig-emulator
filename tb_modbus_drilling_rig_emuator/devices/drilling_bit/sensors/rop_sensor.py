from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class ROPSensor(Sensor):
    def __init__(self, address, speed):
        super().__init__(address)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def update(self):
        pass
