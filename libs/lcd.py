import time
from RPLCD.gpio import CharLCD


class LCD:

    def __init__(self):
        self.text = "0"

        self.lcd = CharLCD(
            pin_rs=15,
            pin_rw=18,
            pin_e=16,
            pins_data=[21, 22, 23, 24],
            # numbering_mode=GPIO.BOARD
        )

    def update_value(self, input_value: str):
        self.text = input_value

    def refresh_screen(self):
        self.lcd.write_string(self.text)

    def clear_screen(self):
        time.sleep(1)
        self.lcd.clear()
