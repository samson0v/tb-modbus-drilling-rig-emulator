from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class EquipmentVibrationSensor(Sensor):
    def __init__(self, address, vibration):
        super().__init__(address)
        self.__vibration = vibration

    @property
    def vibration(self):
        return self.__vibration

    def update(self, vibration):
        self.__vibration = vibration
