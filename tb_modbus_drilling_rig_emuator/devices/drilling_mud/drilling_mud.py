from tb_modbus_drilling_rig_emuator.devices.device import Device
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_gas_cut_sensor import MudGasCutSensor
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_density_sensor import MudDensitySensor
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_flow_rate_sensor import MudFlowRateSensor
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_level_sensor import MudLevelSensor
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_pressure_sensor import MudPressureSensor
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_temperature_sensor import MudTemperatureSensor
from tb_modbus_drilling_rig_emuator.devices.drilling_mud.sensors.mud_volume_sensor import MudVolumeSensor


class DrillingMud(Device):
    def __init__(self):
        super().__init__()

        self.__gas_cut_mud_sensor = MudGasCutSensor(address=1, level=90)
        self.__mud_density_sensor = MudDensitySensor(address=2, density=1.2)
        self.__mud_flow_rate_sensor = MudFlowRateSensor(address=3, speed=40)
        self.__mud_level_sensor = MudLevelSensor(address=4, level=70)
        self.__mud_pressure_sensor = MudPressureSensor(address=5, pressure=30)
        self.__mud_temperature_sensor = MudTemperatureSensor(address=6, temperature=50)
        self.__mud_volume_sensor = MudVolumeSensor(address=7,volume=90)

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"DrillingMud(gas_cut={self.gas_cut}, density={self.density}, flow_rate={self.flow_rate}, " \
               f"level={self.level}, pressure={self.pressure}, temperature={self.temperature}, volume={self.volume})"

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
    def level(self):
        return self.__mud_level_sensor.level

    @property
    def pressure(self):
        return self.__mud_pressure_sensor.pressure

    @property
    def temperature(self):
        return self.__mud_temperature_sensor.temperature

    @property
    def volume(self):
        return self.__mud_volume_sensor.volume

    def update(self):
        self.update_state()

        if self._running:
            self.__mud_level_sensor.update(self.__mud_flow_rate_sensor.speed / 100)

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
