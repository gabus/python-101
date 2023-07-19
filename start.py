import time

from libs.lcd import LCD
from libs.sensor import Sensor

sensor = Sensor()
lcd = LCD()


while True:
    values = sensor.fetch()

    lcd.update_value(str(values))
    lcd.refresh()

    time.sleep(1)
