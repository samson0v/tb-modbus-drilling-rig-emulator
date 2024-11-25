from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class TensionSensor(Sensor):
    def __init__(self, address, tension):
        super().__init__(address)
        self.__tension = tension

    @property
    def tension(self):
        return self.__tension

    def update(self, tension):
        self.__tension = tension
