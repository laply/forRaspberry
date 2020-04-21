import smbus

class PM2008M :
    i2c = smbus.SMBus(1)
    loc = 0x28

    def MySimUartTx(self) :
        self.TxBuffer = [0x11, 0x02, 0x0B, 0x07, 0xDB] 
        for TxCnt in self.TxNumber :
            self.i2c.write_byte(loc, TxCnt)

        print(self.i2c.read_byte(0x28))