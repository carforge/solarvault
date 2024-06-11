# common/device.py

class psu_device:
    def __init__(self, value=None):
        self.interface = value

    def __str__(self):
        return f"Selected serial interface: {self.interface}"

    def mod_if(self, value):
        self.interface = value