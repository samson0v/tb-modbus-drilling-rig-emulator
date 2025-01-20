from random import uniform

from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_RIG_HOOK_LOAD
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class HookLoadSensor(Sensor):
    def __init__(self, address, load):
        super().__init__(address)
        self.__load = load

    @property
    def load(self):
        return self.__load

    def set_init_value(self):
        self.__load = DRILLING_RIG_HOOK_LOAD

    def update(self, load=None):
        if load is not None:
            self.__load = load
            return

        self.__load = int(self.__load + uniform(-2, 2))
