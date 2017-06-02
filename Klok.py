from RPi import GPIO
from datetime import datetime
import smbus

class Ds1307:
    extra_register_1 = 0x08

    def __init__(self, i2cbus=1, address=0x68):
        self.bus = smbus.SMBus(i2cbus)
        self.address = address

    def __read(self, register):
        return self.bus.read_byte_data(self.address, register)


    def __write(self, register, data):
        return self.bus.write_byte_data(self.address, register, data)



    def writeString(self, tekst):
        self.__write(self.extra_register_1, tekst)

    def getString(self):
        string = self.__read(self.extra_register_1)
        return string

    def __StringToASCII(self, data):
        resultaat = ord(data)
        return resultaat


