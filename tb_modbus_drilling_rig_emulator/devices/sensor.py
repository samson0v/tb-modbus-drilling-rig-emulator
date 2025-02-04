from abc import abstractmethod
import random


class Sensor:
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @staticmethod
    def _as_int(value):
        return int(round(value, 1) * 10)

    @staticmethod
    def generate_value(current_value, deviation, min_value, max_value):
        new_number = current_value + random.randint(-deviation, deviation)
        new_number = max(min_value, min(max_value, new_number))

        return new_number
