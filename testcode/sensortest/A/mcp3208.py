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
        reading = [analog_read(0), analog_read(1), analog_read(2), analog_read(3)]
        voltage = [reading[0] * 3.3 / 1024, reading[1] * 3.3 / 1024, reading[2] * 3.3 / 1024, reading[3] * 3.3 / 1024]
        
        for i in reading :
            print("Reading1=%d - Voltage=%f" % (reading[num], voltage[num]))
            num = num + 1
        time.sleep(2)

except KeyboardInterrupt:
    spi.close()
