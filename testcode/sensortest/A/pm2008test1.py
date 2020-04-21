import smbus
import time

i2c = smbus.SMBus(1)
loc = 0x28
TxBuffer = [0x16, 0x7, 0x3, 0xFF, 0xFF, 0, 0x16] 

while True:
    i2c.write_i2c_block_data(loc, 0x50, TxBuffer)  

    value_buffer = i2c.read_i2c_block_data(loc, 0x51)


    if value_buffer[1] == 32 and value_buffer[0] == 0x16 :
        print(value_buffer)
        pm1p0_grimm = (value_buffer[7] << 8) + value_buffer[8]
        pm2p5_grimm = (value_buffer[9] << 8) + value_buffer[10]
        pm10_grimm = (value_buffer[11] << 8) + value_buffer[12]
        pm1p0_tsi = (value_buffer[13] << 8) + value_buffer[14]
        pm2p5_tsi = (value_buffer[15] << 8) + value_buffer[16]
        pm10_tsi = (value_buffer[16] << 8) + value_buffer[18]
        print("pm1.0_grimm: %f "  % (pm1p0_grimm))
        print("pm25_grimm: %f "  % (pm2p5_grimm))
        print("pm10_grimm: %f "  % (pm10_grimm))
        print("pm1.0_tsi: %f "  % (pm1p0_tsi))
        print("pm25_tsi: %f "  % (pm2p5_tsi))
        print("pm10_tsi: %f "  % (pm10_tsi))