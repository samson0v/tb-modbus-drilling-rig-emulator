from tb_modbus_drilling_rig_emuator.devices.device import Device
from tb_modbus_drilling_rig_emuator.devices.drawwork.sensors.cable_length_sensor import CableLengthSensor
from tb_modbus_drilling_rig_emuator.devices.drawwork.sensors.hoist_speed_sensor import HoistSpeedSensor
from tb_modbus_drilling_rig_emuator.devices.drawwork.sensors.inclination_sensor import InclinationSensor
from tb_modbus_drilling_rig_emuator.devices.drawwork.sensors.position_sensor import PositionSensor
from tb_modbus_drilling_rig_emuator.devices.drawwork.sensors.tension_sensor import TensionSensor
from tb_modbus_drilling_rig_emuator.devices.drawwork.sensors.vibration_sensor import VibrationSensor


class Drawwork(Device):
    def __init__(self):
        super().__init__()

        self.__cable_length_sensor = CableLengthSensor(address=1, cable_length=0)
        self.__hoist_speed_sensor = HoistSpeedSensor(address=2, speed=0)
        self.__inclination_sensor = InclinationSensor(address=3, inclination=10)
        self.__position_sensor = PositionSensor(address=4, position=30)
        self.__tension_sensor = TensionSensor(address=5, tension=170)
        self.__vibration_sensor = VibrationSensor(address=6, vibration_level=15)

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"Drawwork(cable_length={self.__cable_length_sensor.cable_length}, hoist_speed={self.__hoist_speed_sensor.speed}, " \
               f"inclination={self.__inclination_sensor.inclination}, position={self.__position_sensor.position}, tension={self.__tension_sensor.tension}, " \
               f"vibration_level={self.__vibration_sensor.vibration_level})"

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

    def update(self):
        self.update_state()

        if self._running:
            self._update_storage(6, self.get_all_sensors_values().values())
