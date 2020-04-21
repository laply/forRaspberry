import smbus

class PM2008M :
    i2c = smbus.SMBus(1)
    loc = 0x28
    TxBuffer = [0x16, 0x7, 0x3, 0xFF, 0xFF, 0, 0x16] 

    def read(self) :
        i2c.write_i2c_block_data(loc, 0x50, TxBuffer) 
        self.value_buffer = i2c.read_i2c_block_data(loc, 0x51)
        
        if value_buffer[1] == 32 and value_buffer[0] == 0x16 :
            self.pm2p5_grimm = (value_buffer[9] << 8) + value_buffer[10]
            self.pm10_grimm = (value_buffer[11] << 8) + value_buffer[12]
            self.pm2p5_tsi = (value_buffer[15] << 8) + value_buffer[16]
            self.pm10_tsi = (value_buffer[17] << 8) + value_buffer[18]

    def getPm2p5Grimm(self):
        return self.pm2p5_grimm

    def getPm10Grimm(self):
        return self.pm10_grimm

    def getPm2p5Tsi(self):
        return self.pm2p5_tsi
    
    def getPm105Tsi(self):
        return self.pm10_tsi