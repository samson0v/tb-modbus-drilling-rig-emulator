from abc import abstractmethod

from pymodbus.datastore import ModbusSlaveContext, ModbusSequentialDataBlock


class Device:
    def __init__(self):
        self._running = False
        self.__storage = ModbusSlaveContext(
            co=ModbusSequentialDataBlock(1, self._create_initial_values([self._running])))

    @abstractmethod
    def get_all_sensors_values(self) -> dict:
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        """
        Update the sensors every time the drilling bit is running (by default every 2 sec)
        """
        pass

    @property
    def storage(self):
        return self.__storage

    @staticmethod
    def _create_initial_values(initial_values):
        return (list(initial_values) or []) + [0] * (16 - len(initial_values or []))

    def on(self):
        self._running = True

        self._on()

    def _on(self):
        self._update_storage(1, {1: True})

    def off(self):
        self._running = False

        self._off()

    def _off(self):
        self._update_storage(1, {1: False})

    def _init_storage(self, sensors_values):
        self.__storage.store['h'] = ModbusSequentialDataBlock(1, self._create_initial_values(sensors_values))

    def _update_storage(self, function_code, values):
        for (address, value) in values.items():
            self.__storage.setValues(function_code, address, [value])

    def _read_storage(self, function_code, address):
        return self.__storage.getValues(function_code, address, count=1)

    def __update_running_status(self):
        running = bool(self._read_storage(1, 1)[0])

        if running != self._running:
            self._running = running

            if running:
                self.on()
            else:
                self.off()

    def update_state(self):
        self.__update_running_status()
