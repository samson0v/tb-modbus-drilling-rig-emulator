from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class CableLengthSensor(Sensor):
    def __init__(self, address, cable_length):
        super().__init__(address)
        self.__cable_length = cable_length

    @property
    def cable_length(self):
        return self.__cable_length

    def update(self):
        pass
