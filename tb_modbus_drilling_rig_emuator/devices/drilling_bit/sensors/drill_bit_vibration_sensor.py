from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class DrillBitVibrationSensor(Sensor):
    def __init__(self, address, vibration_level):
        super().__init__(address)
        self.__vibration_level = vibration_level

    @property
    def vibration_level(self):
        return self.__vibration_level

    def update(self):
        pass
