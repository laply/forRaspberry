import spidev
import time

spi = spidev.SpiDev()

spi.open(0,0)

def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

try :
    while True:
        num = 0
        reading = [analog_read(0), analog_read(1)]
        voltage = [reading[0] * 3.3 / 1024, reading[1] * 3.3 / 1024]
        
        for i in reading :
            print("Reading %d = %d - Voltage = %f" % (num , reading[num], voltage[num]))
            num = num + 1

        print("")

except KeyboardInterrupt:
    spi.close()
