from tb_modbus_drilling_rig_emulator.devices.device import Device
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.sensors.bottom_hole_temperature_sensor import \
    BottomHoleTemperatureSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.sensors.drill_bit_position_sensor import DrillBitPositionSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.sensors.drill_bit_vibration_sensor import \
    DrillBitVibrationSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.sensors.mud_pressure_sensor import MudPressureSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.sensors.rop_sensor import ROPSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_bit.sensors.well_depth_sensor import WellDepthSensor


class DrillingBit(Device):
    def __init__(self, input_drilling_speed):
        super().__init__()

        self.__bottom_hole_temperature_sensor = BottomHoleTemperatureSensor(address=1, temperature=0)
        self.__drill_bit_position_sensor = DrillBitPositionSensor(address=2, position=0)
        self.__drill_bit_vibration_sensor = DrillBitVibrationSensor(address=3, vibration_level=20)
        self.__mud_pressure_sensor = MudPressureSensor(address=4, pressure=25)
        self.__rop_sensor = ROPSensor(address=5, speed=input_drilling_speed)
        self.__well_depth_sensor = WellDepthSensor(address=6)

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"DrillingBit(current_depth={self.current_depth}, temperature={self.temperature}, " \
               f"vibration_level={self.vibration_level}, position={self.position}, pressure={self.pressure}, " \
               f"speed={self.speed})"

    @property
    def current_depth(self):
        return self.__well_depth_sensor.current_depth

    @property
    def temperature(self):
        return self.__bottom_hole_temperature_sensor.temperature

    @property
    def vibration_level(self):
        return self.__drill_bit_vibration_sensor.vibration_level

    @property
    def position(self):
        return self.__drill_bit_position_sensor.position

    @property
    def pressure(self):
        return self.__mud_pressure_sensor.pressure

    @property
    def speed(self):
        return self.__rop_sensor.speed

    def off(self):
        self.__rop_sensor.speed = 0

        super().off()

    def update(self, is_drilling_fluid_supplied):
        self.update_state()

        if self._running:
            self.__bottom_hole_temperature_sensor.update(is_drilling_fluid_supplied)
            self.__well_depth_sensor.update(self.__rop_sensor.speed)
            self.__drill_bit_position_sensor.update(self.__well_depth_sensor.current_depth + 0.2)

            self._update_storage(6, self.get_all_sensors_values())

    def get_all_sensors_values(self):
        return {
            self.__bottom_hole_temperature_sensor.address: self.__bottom_hole_temperature_sensor.temperature,
            self.__drill_bit_position_sensor.address: self.__drill_bit_position_sensor.position,
            self.__drill_bit_vibration_sensor.address: self.__drill_bit_vibration_sensor.vibration_level,
            self.__mud_pressure_sensor.address: self.__mud_pressure_sensor.pressure,
            self.__rop_sensor.address: self.__rop_sensor.speed,
            self.__well_depth_sensor.address: self.__well_depth_sensor.current_depth
        }
