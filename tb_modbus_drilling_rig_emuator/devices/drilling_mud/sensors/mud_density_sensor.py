from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class MudDensitySensor(Sensor):
    def __init__(self, address, density):
        super().__init__(address)
        self.__density = density

    @property
    def density(self):
        return self._as_int(self.__density)

    @density.setter
    def density(self, density):
        self.__density = density

    def update(self):
        pass
