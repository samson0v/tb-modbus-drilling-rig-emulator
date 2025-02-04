from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRAWWORK_INCLINATION_MAX, DRAWWORK_INCLINATION_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class InclinationSensor(Sensor):
    def __init__(self, address, inclination):
        super().__init__(address)
        self.__inclination = inclination

    @property
    def inclination(self):
        return self.__inclination

    def update(self, inclination=None):
        if inclination is not None:
            self.__inclination = inclination

        self.__inclination = self.generate_value(self.__inclination, 2, DRAWWORK_INCLINATION_MIN, DRAWWORK_INCLINATION_MAX)
