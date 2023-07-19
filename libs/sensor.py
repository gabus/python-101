import random


class Sensor:

    def fetch(self) -> float:
        return random.randint(0, 100)
