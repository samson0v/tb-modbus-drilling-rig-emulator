from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class MudGasCutSensor(Sensor):
    def __init__(self, address, level):
        super().__init__(address)
        self.__level = level

    @property
    def level(self):
        return self.__level

    def update(self):
        pass