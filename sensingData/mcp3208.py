import spidev
import time

class MCP3208 :
    
    def __init__(self, usePin):
        self.spi = spidev.SpiDev()
        self.usePin = usePin
        self.spi.open(0, 1)

    def analogRead(self, channel):
        r = self.spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1]&3) << 8) + r[2]
        return adc_out

    def getVoltage(self, read) :
        return read * 3.3 / 1024
