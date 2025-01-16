from abc import abstractmethod


class Sensor:
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @staticmethod
    def _as_int(value):
        return int(round(value, 1) * 10)
