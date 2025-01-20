from tb_modbus_drilling_rig_emulator.devices.device import Device
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.equipment_temperature_sensor import \
    EquipmentTemperatureSensor
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.equipment_vibration_sensor import EquipmentVibrationSensor
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.flow_rate_sensor import FlowRateSensor
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.gas_cut_mud_sensor import GasCutMudSensor
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.mud_temperature_sensor import MudTemperatureSensor
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.system_leak_detection_sensor import \
    SystemLeakDetectionSensor
from tb_modbus_drilling_rig_emulator.devices.preventer.sensors.well_pressure_sensor import WellPressureSensor


class Preventer(Device):
    def __init__(self):
        super().__init__()

        self.__equipment_temperature_sensor = EquipmentTemperatureSensor(address=1, temperature=0)
        self.__equipment_vibration_sensor = EquipmentVibrationSensor(address=2, vibration=0)
        self.__mud_temperature_sensor = MudTemperatureSensor(address=3, temperature=0)
        self.__flow_rate_sensor = FlowRateSensor(address=4, flow_rate=0)
        self.__gas_cut_mud_sensor = GasCutMudSensor(address=5, level=0)
        self.__system_leak_detection_sensor = SystemLeakDetectionSensor(address=6, level=0)
        self.__well_pressure_sensor = WellPressureSensor(address=7, pressure=0)

        self._init_storage(self.get_all_sensors_values().values())

    def __str__(self):
        return f"Preventer(temperature={self.__equipment_temperature_sensor.temperature}, vibration={self.__equipment_vibration_sensor.vibration}, mud_temperature={self.__mud_temperature_sensor.temperature}, " \
               f"flow_rate={self.__flow_rate_sensor.flow_rate}, gas_cut={self.__gas_cut_mud_sensor.level}, leak_detection={self.__system_leak_detection_sensor.level}, pressure={self.__well_pressure_sensor.pressure})"

    @property
    def status(self):
        return self._running

    @property
    def temperature(self):
        return self.__equipment_temperature_sensor.temperature

    @property
    def vibration(self):
        return self.__equipment_vibration_sensor.vibration

    @property
    def mud_temperature(self):
        return self.__mud_temperature_sensor.temperature

    @property
    def flow_rate(self):
        return self.__flow_rate_sensor.flow_rate

    @property
    def gas_cut(self):
        return self.__gas_cut_mud_sensor.level

    @property
    def leak_detection(self):
        return self.__system_leak_detection_sensor.level

    @property
    def pressure(self):
        return self.__well_pressure_sensor.pressure

    def on(self):
        super().on()

        self.__equipment_temperature_sensor.set_init_value()
        self.__equipment_vibration_sensor.set_init_value()
        self.__mud_temperature_sensor.set_init_value()
        self.__flow_rate_sensor.set_init_value()
        self.__gas_cut_mud_sensor.set_init_value()
        self.__system_leak_detection_sensor.set_init_value()
        self.__well_pressure_sensor.set_init_value()

    def off(self):
        super().off()

        self.__equipment_temperature_sensor.update(temperature=0)
        self.__equipment_vibration_sensor.update(vibration=0)
        self.__mud_temperature_sensor.update(temperature=0)
        self.__flow_rate_sensor.update(flow_rate=0)
        self.__gas_cut_mud_sensor.update(level=0)
        self.__system_leak_detection_sensor.update(level=0)
        self.__well_pressure_sensor.update(pressure=0)

        self._update_storage(6, self.get_all_sensors_values())

    def update(self):
        self.update_state()

        if self._running:
            self.__equipment_temperature_sensor.update()
            self.__equipment_vibration_sensor.update()
            self.__mud_temperature_sensor.update()
            self.__flow_rate_sensor.update()
            self.__gas_cut_mud_sensor.update()
            self.__system_leak_detection_sensor.update()
            self.__well_pressure_sensor.update()

            self._update_storage(6, self.get_all_sensors_values())

    def get_all_sensors_values(self) -> dict:
        return {
            self.__equipment_temperature_sensor.address: self.__equipment_temperature_sensor.temperature,
            self.__equipment_vibration_sensor.address: self.__equipment_vibration_sensor.vibration,
            self.__mud_temperature_sensor.address: self.__mud_temperature_sensor.temperature,
            self.__flow_rate_sensor.address: self.__flow_rate_sensor.flow_rate,
            self.__gas_cut_mud_sensor.address: self.__gas_cut_mud_sensor.level,
            self.__system_leak_detection_sensor.address: self.__system_leak_detection_sensor.level,
            self.__well_pressure_sensor.address: self.__well_pressure_sensor.pressure
        }
