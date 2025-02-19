from tb_modbus_drilling_rig_emulator.devices.device import Device
from tb_modbus_drilling_rig_emulator.devices.drawwork.sensors.cable_length_sensor import CableLengthSensor
from tb_modbus_drilling_rig_emulator.devices.drawwork.sensors.hoist_speed_sensor import HoistSpeedSensor
from tb_modbus_drilling_rig_emulator.devices.drawwork.sensors.inclination_sensor import InclinationSensor
from tb_modbus_drilling_rig_emulator.devices.drawwork.sensors.position_sensor import PositionSensor
from tb_modbus_drilling_rig_emulator.devices.drawwork.sensors.tension_sensor import TensionSensor
from tb_modbus_drilling_rig_emulator.devices.drawwork.sensors.vibration_sensor import VibrationSensor


class Drawwork(Device):
    def __init__(self):
        super().__init__()

        self.direction = False
        self.drawwork_speed = False
        self.__cable_length_sensor = CableLengthSensor(address=1, cable_length=100)
        self.__hoist_speed_sensor = HoistSpeedSensor(address=2, speed=5)
        self.__inclination_sensor = InclinationSensor(address=3, inclination=6)
        self.__position_sensor = PositionSensor(address=4, position=0)
        self.__tension_sensor = TensionSensor(address=5, tension=170)
        self.__vibration_sensor = VibrationSensor(address=6, vibration_level=15)

        self._init_storage(self.get_all_sensors_values().values())
        self._init_storage([self.direction, self.drawwork_speed], registers_type='c', from_address=2)

    def __str__(self):
        return f"Drawwork(cable_length={self.__cable_length_sensor.cable_length}, hoist_speed={self.__hoist_speed_sensor.speed}, " \
               f"inclination={self.__inclination_sensor.inclination}, position={self.__position_sensor.position} " \
               f"vibration_level={self.__vibration_sensor.vibration_level}, tension={self.__tension_sensor.tension})"

    @property
    def status(self):
        return self._running

    @property
    def cable_length(self):
        return self.__cable_length_sensor.cable_length

    @property
    def hoist_speed(self):
        return self.__hoist_speed_sensor.speed

    @property
    def inclination(self):
        return self.__inclination_sensor.inclination

    @property
    def position(self):
        return self.__position_sensor.position

    @property
    def tension(self):
        return self.__tension_sensor.tension

    @property
    def vibration_level(self):
        return self.__vibration_sensor.vibration_level

    def get_all_sensors_values(self) -> dict:
        return {
            self.__cable_length_sensor.address: self.__cable_length_sensor.cable_length,
            self.__hoist_speed_sensor.address: self.__hoist_speed_sensor.speed,
            self.__inclination_sensor.address: self.__inclination_sensor.inclination,
            self.__position_sensor.address: self.__position_sensor.position,
            self.__tension_sensor.address: self.__tension_sensor.tension,
            self.__vibration_sensor.address: self.__vibration_sensor.vibration_level
        }

    def update(self, position):
        self.update_state()

        if self._running:
            self.__position_sensor.update(position, self.direction, self.__hoist_speed_sensor.speed)
            self.__inclination_sensor.update()
            self.__tension_sensor.update()
            self.__vibration_sensor.update()
            self._update_storage(6, self.get_all_sensors_values())

    def update_state(self):
        super().update_state()

        self.__update_direction_state()
        self.__update_drawwork_speed()

    def __update_direction_state(self):
        direction = bool(self._read_storage(1, 2)[0])

        if direction != self.direction:
            self.direction = direction

    def __update_drawwork_speed(self):
        drawwork_speed = bool(self._read_storage(1, 3)[0])

        if drawwork_speed != self.drawwork_speed:
            self.drawwork_speed = drawwork_speed

            if self.drawwork_speed:
                self.__set_normal_speed()
            else:
                self.__set_slow_speed()

    def __set_slow_speed(self):
        self.__hoist_speed_sensor.update(3)

    def __set_normal_speed(self):
        self.__hoist_speed_sensor.update(12)
