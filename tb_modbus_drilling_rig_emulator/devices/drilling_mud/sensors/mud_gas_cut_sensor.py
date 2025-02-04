from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_GAS_CUT, DRILLING_MUD_GAS_CUT_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudGasCutSensor(Sensor):
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

        self.__level = self.generate_value(self.__level, 1, DRILLING_MUD_GAS_CUT_MIN, DRILLING_MUD_GAS_CUT_MIN)

    def set_init_value(self):
        self.__level = DRILLING_MUD_GAS_CUT
