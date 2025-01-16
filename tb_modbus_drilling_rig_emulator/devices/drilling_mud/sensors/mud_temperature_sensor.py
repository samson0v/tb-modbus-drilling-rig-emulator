from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudTemperatureSensor(Sensor):
    def __init__(self, address, temperature):
        super().__init__(address)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def update(self):
        pass
