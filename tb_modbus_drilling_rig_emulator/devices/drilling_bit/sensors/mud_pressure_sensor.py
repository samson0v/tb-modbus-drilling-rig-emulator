from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudPressureSensor(Sensor):
    def __init__(self, address, pressure):
        super().__init__(address)
        self.__pressure = pressure

    @property
    def pressure(self):
        return self.__pressure

    def update(self):
        pass
