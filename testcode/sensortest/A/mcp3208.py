import spidev
import time

spi = spidev.SpiDev()

spi.open(0, 1)
spi.max_speed_hz = 1000000

def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

try :
    while True:
        num = 0
        reading = analog_read(num)
        voltage = reading * 3.3 / 1024
	print("Reading = %d - Voltage = %f" % (reading, voltage))

        print("")
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
