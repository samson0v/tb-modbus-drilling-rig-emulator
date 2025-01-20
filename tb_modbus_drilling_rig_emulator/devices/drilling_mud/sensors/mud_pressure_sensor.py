from random import uniform
from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_PRESSURE
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudPressureSensor(Sensor):
    def __init__(self, address, pressure):
        super().__init__(address)
        self.__pressure = pressure

    @property
    def pressure(self):
        return self.__pressure

    def update(self, pressure=None):
        if pressure is not None:
            self.__pressure = pressure
            return

        self.__pressure = int(self.__pressure + uniform(-3, 3))

    def set_init_value(self):
        self.__pressure = DRILLING_MUD_PRESSURE
