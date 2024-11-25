from tb_modbus_drilling_rig_emuator.devices.sensor import Sensor


class FlowRateSensor(Sensor):
    def __init__(self, address, flow_rate):
        super().__init__(address)
        self.__flow_rate = flow_rate

    @property
    def flow_rate(self):
        return self.__flow_rate

    def update(self, flow_rate):
        self.__flow_rate = flow_rate
