import time
import random


class Sensor:

    def fetch(self) -> float:
        time.sleep(0.2)  # simulate overhead (and use sleep)
        return random.randint(0, 100)
