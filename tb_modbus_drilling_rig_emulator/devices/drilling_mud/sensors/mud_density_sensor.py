from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRILLING_MUD_DENSITY, DRILLING_MUD_DENSITY_MAX, DRILLING_MUD_DENSITY_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudDensitySensor(Sensor):
    def __init__(self, address, density):
        super().__init__(address)
        self.__density = density

    @property
    def density(self):
        return self._as_int(self.__density / 10)

    @density.setter
    def density(self, density):
        self.__density = density

    def update(self, density=None):
        if density is not None:
            self.__density = density
            return

        self.__density = self.generate_value(self.__density, 1, DRILLING_MUD_DENSITY_MIN, DRILLING_MUD_DENSITY_MAX)

    def set_init_value(self):
        self.__density = DRILLING_MUD_DENSITY
