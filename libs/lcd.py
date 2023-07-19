class LCD:

    def __init__(self):
        self.value = "0"

    def update_value(self, input_value: str):
        self.value = input_value

    def refresh(self):
        print(self.value)
