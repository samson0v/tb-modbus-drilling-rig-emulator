from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class BottomHoleTemperatureSensor(Sensor):
    def __init__(self, address, temperature):
        super().__init__(address)
        self.temperature = temperature

    def update(self, is_drilling_fluid_supplied):
        if self.temperature >= 200 and not is_drilling_fluid_supplied:
            raise ValueError("Drilling bit temperature is too high")

        if is_drilling_fluid_supplied and self.temperature <= 150:
            self.__increase_temperature(1)
        elif is_drilling_fluid_supplied and self.temperature > 150:
            self.__decrease_temperature(1)
        elif not is_drilling_fluid_supplied:
            self.__increase_temperature(10)

    def __increase_temperature(self, value):
        self.temperature += value

    def __decrease_temperature(self, value):
        self.temperature -= value
