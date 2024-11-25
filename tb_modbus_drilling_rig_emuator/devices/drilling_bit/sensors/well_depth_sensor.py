from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class WellDepthSensor(Sensor):
    def __init__(self, address):
        super().__init__(address)
        self.__current_depth = 0

    @property
    def current_depth(self):
        return self.__current_depth

    def update(self, speed):
        self.__current_depth += speed
