import smbus
import time

i2c = smbus.SMBus(1)
loc = 0x28
TxBuffer = [0x11, 0x02, 0x0B, 0x07, 0xDB] 

i2c.write_i2c_block_data(loc, 0x16, TxBuffer)  

value_buffer = i2c.read_i2c_block_data(0x28, 0x16)


pm1p0_grimm = (value_buffer[7] << 8 + value_buffer[8])
pm2p5_grimm = (value_buffer[9] << 8 + value_buffer[10])
pm10_grimm = (value_buffer[11] << 8 + value_buffer[12])
pm1p0_tsi = value_buffer[13] << 8 + value_buffer[14]
pm2p5_tsi = value_buffer[15] << 8 + value_buffer[16]
pm10_tsi = value_buffer[16] << 8 + value_buffer[18]
print("pm1.0_grimm: %f "  % (pm1p0_grimm))
print("pm25_grimm: %f "  % (pm2p5_grimm))
print("pm10_grimm: %f "  % (pm10_grimm))