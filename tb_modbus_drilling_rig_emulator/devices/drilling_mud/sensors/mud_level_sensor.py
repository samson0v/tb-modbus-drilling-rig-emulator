from tb_modbus_drilling_rig_emulator.devices.sensor import Sensor


class MudLevelSensor(Sensor):
    def __init__(self, address, level):
        super().__init__(address)
        self.__level = level

    @property
    def level(self):
        return self._as_int(self.__level)

    def update(self, level):
        self.__level -= level

        if self.__level <= 10:
            raise ValueError("Mud level is too low")

        if self.__level >= 100:
            raise ValueError("Mud level is too high")
