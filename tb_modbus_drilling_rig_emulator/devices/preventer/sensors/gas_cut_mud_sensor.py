from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTED_GAS_CUT, PREVENTED_GAS_CUT_MAX, PREVENTED_GAS_CUT_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class GasCutMudSensor(Sensor):
    def __init__(self, address, level):
        super().__init__(address)
        self.__level = level

    @property
    def level(self):
        return self.__level

    def update(self, level=None):
        if level is not None:
            self.__level = level
            return

        self.__level = self.generate_value(self.__level, 1, PREVENTED_GAS_CUT_MIN, PREVENTED_GAS_CUT_MAX)

    def set_init_value(self):
        self.__level = PREVENTED_GAS_CUT
