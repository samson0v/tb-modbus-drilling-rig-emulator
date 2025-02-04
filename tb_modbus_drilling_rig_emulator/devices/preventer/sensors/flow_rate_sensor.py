from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_FLOW_RATE, PREVENTER_FLOW_RATE_MAX, PREVENTER_FLOW_RATE_MIN
from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class FlowRateSensor(Sensor):
    def __init__(self, address, flow_rate):
        super().__init__(address)
        self.__flow_rate = flow_rate

    @property
    def flow_rate(self):
        return self.__flow_rate

    def update(self, flow_rate=None):
        if flow_rate is not None:
            self.__flow_rate = flow_rate
            return

        self.__flow_rate = self.generate_value(self.__flow_rate, 1, PREVENTER_FLOW_RATE_MIN, PREVENTER_FLOW_RATE_MAX)

    def set_init_value(self):
        self.__flow_rate = PREVENTER_FLOW_RATE
