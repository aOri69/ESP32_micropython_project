from machine import SDCard, Pin
from os import mount, umount


class SD:

    def __init__(self, slot=2, pin=4, mount_folder="/sd") -> None:
        self.__sd = SDCard(slot=slot, cs=Pin(pin))

    def __del__(self):
        del self.__sd

    def mount(self, path):
        mount(self.__sd, path)

    def unmount(self, path):
        umount(self.__sd, path)
