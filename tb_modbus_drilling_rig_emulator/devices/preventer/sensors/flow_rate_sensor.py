from random import uniform
from tb_modbus_drilling_rig_emulator.devices.initial_sensors_values import PREVENTER_FLOW_RATE
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

        self.__flow_rate = int(self.__flow_rate + uniform(-1, 1))

    def set_init_value(self):
        self.__flow_rate = PREVENTER_FLOW_RATE
