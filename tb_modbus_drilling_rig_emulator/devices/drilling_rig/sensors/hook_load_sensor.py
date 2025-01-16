from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class HookLoadSensor(Sensor):
    def __init__(self, address, load):
        super().__init__(address)
        self.__load = load

    @property
    def load(self):
        return self.__load

    def update(self):
        pass
