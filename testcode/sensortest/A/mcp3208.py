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

        reading0 = analog_read(0)
        voltage0 = reading0 * 3.3 / 1024

        print("Reading1=%d - Voltage=%f" % (reading0, voltage0))

        time.sleep(2)

except KeyboardInterrupt:
    spi.close()
