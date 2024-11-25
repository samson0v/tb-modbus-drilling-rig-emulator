from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class MudVolumeSensor(Sensor):
    def __init__(self, address, volume):
        super().__init__(address)
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    def update(self):
        pass
