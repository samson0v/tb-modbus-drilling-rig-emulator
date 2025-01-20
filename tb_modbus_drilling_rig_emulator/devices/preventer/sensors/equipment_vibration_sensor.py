from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_EQUIPMENT_TEMPERATURE
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class EquipmentVibrationSensor(Sensor):
    def __init__(self, address, vibration):
        super().__init__(address)
        self.__vibration = vibration

    @property
    def vibration(self):
        return self.__vibration

    def update(self, vibration=None):
        if vibration is not None:
            self.__vibration = vibration
            return

        self.__vibration = int(self.__vibration + uniform(-1, 1))

    def set_init_value(self):
        self.__vibration = PREVENTER_EQUIPMENT_TEMPERATURE
