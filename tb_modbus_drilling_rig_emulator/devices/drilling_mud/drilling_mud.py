from tb_modbus_drilling_rig_emulator.devices.device import Device
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_gas_cut_sensor import MudGasCutSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_density_sensor import MudDensitySensor
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_flow_rate_sensor import MudFlowRateSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_level_sensor import MudLevelSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_pressure_sensor import MudPressureSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_temperature_sensor import MudTemperatureSensor
from tb_modbus_drilling_rig_emulator.devices.drilling_mud.sensors.mud_volume_sensor import MudVolumeSensor


class DrillingMud(Device):
    def __init__(self):
        super().__init__()

        self.__gas_cut_mud_sensor = MudGasCutSensor(address=1, level=0)
        self.__mud_density_sensor = MudDensitySensor(address=2, density=0)
        self.__mud_flow_rate_sensor = MudFlowRateSensor(address=3, speed=0)
        self.__mud_volume_sensor = MudVolumeSensor(address=7, volume=1000)  # Tank Capacity
        self.__mud_level_sensor = MudLevelSensor(address=4,
                                                 tank_capacity=self.__mud_volume_sensor.volume)
        self.__mud_pressure_sensor = MudPressureSensor(address=5, pressure=0)
        self.__mud_temperature_sensor = MudTemperatureSensor(address=6, temperature=0)
        self.__valve = False

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"DrillingMud(gas_cut={self.gas_cut}, density={self.density}, flow_rate={self.flow_rate}, " \
            f"capacity={self.capacity}, pressure={self.pressure}, temperature={self.temperature}, " \
            f"current_volume={self.current_volume}), valve={self.__valve}"

    @property
    def status(self):
        return self._running

    @property
    def gas_cut(self):
        return self.__gas_cut_mud_sensor.level

    @property
    def density(self):
        return self.__mud_density_sensor.density

    @property
    def flow_rate(self):
        return self.__mud_flow_rate_sensor.speed

    @property
    def current_volume(self):
        return self.__mud_level_sensor.level

    @property
    def pressure(self):
        return self.__mud_pressure_sensor.pressure

    @property
    def temperature(self):
        return self.__mud_temperature_sensor.temperature

    @property
    def capacity(self):
        return self.__mud_volume_sensor.volume

    def on(self):
        super().on()

        self.__valve = True
        self._update_storage(1, {2: self.__valve})

        self.__mud_temperature_sensor.set_init_value()
        self.__gas_cut_mud_sensor.set_init_value()
        self.__mud_pressure_sensor.set_init_value()
        self.__mud_density_sensor.set_init_value()
        self.__mud_flow_rate_sensor.set_init_value()

    def off(self):
        super().off()

        self.__valve = False
        self._update_storage(1, {2: self.__valve})

        self.__mud_temperature_sensor.update(temperature=0)
        self.__gas_cut_mud_sensor.update(level=0)
        self.__mud_pressure_sensor.update(pressure=0)
        self.__mud_density_sensor.update(density=0)
        self.__mud_flow_rate_sensor.update(speed=0)

        self._update_storage(6, self.get_all_sensors_values())

    def update(self):
        self.update_state()

        if self._running:
            self.__mud_level_sensor.update()
            self.__mud_temperature_sensor.update()
            self.__gas_cut_mud_sensor.update()
            self.__mud_pressure_sensor.update()
            self.__mud_density_sensor.update()
            self.__mud_flow_rate_sensor.update()

            self._update_storage(6, self.get_all_sensors_values())

    def get_all_sensors_values(self):
        return {
            self.__gas_cut_mud_sensor.address: self.__gas_cut_mud_sensor.level,
            self.__mud_density_sensor.address: self.__mud_density_sensor.density,
            self.__mud_flow_rate_sensor.address: self.__mud_flow_rate_sensor.speed,
            self.__mud_level_sensor.address: self.__mud_level_sensor.level,
            self.__mud_pressure_sensor.address: self.__mud_pressure_sensor.pressure,
            self.__mud_temperature_sensor.address: self.__mud_temperature_sensor.temperature,
            self.__mud_volume_sensor.address: self.__mud_volume_sensor.volume
        }
