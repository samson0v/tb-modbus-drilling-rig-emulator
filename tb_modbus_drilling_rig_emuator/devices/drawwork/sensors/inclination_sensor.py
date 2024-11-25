from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class InclinationSensor(Sensor):
    def __init__(self, address, inclination):
        super().__init__(address)
        self.__inclination = inclination

    @property
    def inclination(self):
        return self.__inclination

    def update(self, inclination):
        self.__inclination = inclination
