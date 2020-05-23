from machine import SDCard, Pin
from os import mount, umount

class SD:

    def __init__(self, slot=2, pin=4) -> None:
        self.sd = SDCard(slot=slot, cs=Pin(pin))

    def __del__(self):
        self.sd.__del__()

    def deinit(self):
        self.sd.deinit()

    def mount(self, path="/sd"):
        mount(self.sd, path)

    def umount(self, path="/sd"):
        umount(path)
