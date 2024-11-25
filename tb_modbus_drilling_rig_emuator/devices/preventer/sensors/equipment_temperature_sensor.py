from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class EquipmentTemperatureSensor(Sensor):
    def __init__(self, address, temperature):
        super().__init__(address)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def update(self, temperature):
        self.__temperature = temperature
