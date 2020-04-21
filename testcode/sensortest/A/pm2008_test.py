import smbus

i2c = smbus.SMBus(1)
loc = 0x28

TxBuffer = [0x11, 0x02, 0x0B, 0x07, 0xDB] 

for TxCnt in TxBuffer :
    i2c.write_byte(loc, TxCnt)

print(i2c.read_byte(0x28))