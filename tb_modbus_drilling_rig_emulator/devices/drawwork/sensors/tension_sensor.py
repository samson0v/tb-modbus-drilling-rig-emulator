from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import DRAWWORK_TENSION_MAX, DRAWWORK_TENSION_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class TensionSensor(Sensor):
    def __init__(self, address, tension):
        super().__init__(address)
        self.__tension = tension

    @property
    def tension(self):
        return self.__tension

    def update(self, tension=None):
        if tension is not None:
            self.__tension = tension

        self.__tension = self.generate_value(self.__tension, 2, DRAWWORK_TENSION_MIN, DRAWWORK_TENSION_MAX)
