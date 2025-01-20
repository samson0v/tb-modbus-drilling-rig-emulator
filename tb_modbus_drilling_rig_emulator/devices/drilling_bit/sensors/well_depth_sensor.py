from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class WellDepthSensor(Sensor):
    def __init__(self, address, depth):
        super().__init__(address)
        self.__well_depth = depth

    @property
    def well_depth(self):
        return self.__well_depth
