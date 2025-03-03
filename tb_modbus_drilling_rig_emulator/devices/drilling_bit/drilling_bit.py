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
    def __init__(self, input_drilling_depth, input_drilling_speed):
        super().__init__()

        self.__bottom_hole_temperature_sensor = BottomHoleTemperatureSensor(address=1, temperature=0)
        self.__drill_bit_position_sensor = DrillBitPositionSensor(address=2, position=0)
        self.__drill_bit_vibration_sensor = DrillBitVibrationSensor(address=3, vibration_level=0)
        self.__mud_pressure_sensor = MudPressureSensor(address=4, pressure=0)
        self.__rop_sensor = ROPSensor(address=5, speed=input_drilling_speed)
        self.__well_depth_sensor = WellDepthSensor(address=6, depth=input_drilling_depth)

        self.__bottom_hole_temperature_sensor.set_init_value()
        self.__drill_bit_vibration_sensor.set_init_value()
        self.__mud_pressure_sensor.set_init_value()

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"DrillingBit(current_depth={self.current_depth}, well_depth={self.well_depth}, " \
               f"vibration_level={self.vibration_level}, pressure={self.pressure}, temperature={self.temperature}, " \
               f"speed={self.speed}), state={self._running}"

    @property
    def current_depth(self):
        return self.__drill_bit_position_sensor.position

    @property
    def temperature(self):
        return self.__bottom_hole_temperature_sensor.temperature

    @property
    def vibration_level(self):
        return self.__drill_bit_vibration_sensor.vibration_level

    @property
    def pressure(self):
        return self.__mud_pressure_sensor.pressure

    @property
    def speed(self):
        return self.__rop_sensor.speed

    @property
    def well_depth(self):
        return self.__well_depth_sensor.well_depth

    def is_running(self):
        return self._running

    def on(self):
        super().on()

        self.__bottom_hole_temperature_sensor.set_init_value()
        self.__drill_bit_vibration_sensor.set_init_value()
        self.__mud_pressure_sensor.set_init_value()

    def off(self):
        super().off()

        self.__drill_bit_vibration_sensor.update(0)
        self.__mud_pressure_sensor.update(0)

        self._update_storage(6, self.get_all_sensors_values())

    def __update_speed_state(self):
        drilling_speed = self._read_storage(3, 5)[0]

        if drilling_speed != self.__rop_sensor.speed and drilling_speed > 0 \
                and (drilling_speed - self.__rop_sensor.speed) <= 1000:
            self.__rop_sensor.speed = drilling_speed

    def __update_well_depth_state(self):
        well_depth = self._read_storage(3, 6)[0]

        if well_depth != self.__well_depth_sensor.well_depth and well_depth > 0:
            self.__well_depth_sensor.well_depth = well_depth
            self.__drill_bit_position_sensor.reset()

    def update_state(self):
        super().update_state()

        self.__update_well_depth_state()
        self.__update_speed_state()

    def update(self, is_drilling_fluid_supplied, is_drawwork_on, drawwork_direction):
        self.update_state()

        if self._running and not drawwork_direction and is_drawwork_on:
            self.__bottom_hole_temperature_sensor.update(is_drilling_fluid_supplied)
            self.__drill_bit_position_sensor.update(self.__rop_sensor.speed)
            self.__drill_bit_vibration_sensor.update()
            self.__mud_pressure_sensor.update(is_drilling_fluid_supplied=is_drilling_fluid_supplied)
        else:
            self.__bottom_hole_temperature_sensor.cooling()

        self._update_storage(6, self.get_all_sensors_values())

    def get_all_sensors_values(self):
        return {
            self.__bottom_hole_temperature_sensor.address: self.__bottom_hole_temperature_sensor.temperature,
            self.__drill_bit_position_sensor.address: self.__drill_bit_position_sensor.position,
            self.__drill_bit_vibration_sensor.address: self.__drill_bit_vibration_sensor.vibration_level,
            self.__mud_pressure_sensor.address: self.__mud_pressure_sensor.pressure,
            self.__rop_sensor.address: self.__rop_sensor.speed,
            self.__well_depth_sensor.address: self.__well_depth_sensor.well_depth
        }
