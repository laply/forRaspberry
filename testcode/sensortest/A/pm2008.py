

class PM2008M :
    def MySimUartTx(self) :
        self.TxNumber = 7 
    # MyPM.MyUart.TxBuffer[0] = 0x11; 
        self.TxBuffer = [0x11, 0x02, 0x0B, 0x07, 0xDB] 
        for TxCnt in TxNumber :
            MySimUart_TxByte(self.TxBuffer[TxCnt]); 
            #MyPM.MyUart.TxBuffer[TxCnt] = 0;
            self.TxBuffer[TxCnt] = 0


#interrupt void USCI0RX_ISR(void)  // from sensor 
    def USCI0RX_ISR(self):
        unsigned char cRxChar0; 
        cRXCount1 = 0
        cRXCount2 = 0
        cRxChar0 = UCA0RXBUF; 
        if Whole_Flag.Rx_Sensor_Scan_Flag == 0 & g_SHighPriority.Flag == 0 : 
            RevDat1[cRXCount1] = cRxChar0
        if RevDat1[0] == 0x16 : # //"id" 
            if cRXCount1 >= 3 and RevDat1[1] == (cRXCount1 - 2): 
                Whole_Flag.Rx_Sensor_Scan_Flag = 1 
                cRXCount1  = 0
                return 

            cRXCount1++ 
            if cRXCount1 >= RX_SENSOR_LEN : 
                cRXCount1 = 0 
        else :
            cRXCount1 = 0 

    def Rx_Scan_Sensor():         #        // Receive Sensor data in scan mode 
        i, checksum = 0
        temprx[30] = {0}

        temprx[1] = RevDat1[1]
        for i in temprx[1]+3 : 
            temprx[i] = RevDat1[i]
            checksum += temprx[i] 
            RevDat1[i] = 0
 
            if temprx[0] != 0x16) or checksum!=0 #   // acceptance error 
                return
        
            RxResDetect(1)
    
            if temprx[2] == CMD_READ_DUST_DATA:  #// 0B command, read command of particle measuring 
                if SucessResSerial == ReadDUST_All :
                    MyPMPoint.GRIMMPMValue[PM10] = (temprx [5] << 8) | temprx [6]; 
                    MyPMPoint.GRIMMPMValue[PM25] = (temprx [9] << 8) | temprx [10]; 
                    MyPMPoint.GRIMMPMValue[PM100] = (temprx [13] << 8) | temprx [14]; 
                    MyPMPoint.TSIPMValue[PM10] = (temprx [17] << 8) | temprx [18]; 
                    MyPMPoint.TSIPMValue[PM25] = (temprx [21] << 8) | temprx [22]; 
                    MyPMPoint.TSIPMValue[PM100] = (temprx [25] << 8) | temprx [26]; 
                    MyPMPoint.CountValue[UM03] = (temprx [29] << 24) | (temprx [30] << 16) | (temprx [31] << 8) | temprx [32]; 
                    MyPMPoint.CountValue[UM05] = (temprx [33] << 24) | (temprx [34] << 16) | (temprx [35] << 8) | temprx [36]; 
                    MyPMPoint.CountValue[UM10] = (temprx [37] << 24) | (temprx [38] << 16) | (temprx [39] << 8) | temprx [40]; 
                    MyPMPoint.CountValue[UM25] = (temprx [41] << 24) | (temprx [42] << 16) | (temprx [43] << 8) | temprx [44]; 
                    MyPMPoint.CountValue[UM50] = (temprx [45] << 24) | (temprx [46] << 16) | (temprx [47] << 8) | temprx [48]; 
                    MyPMPoint.CountValue[UM100] = (temprx [49] << 24) | (temprx [50] << 16) | (temprx [51] << 8) | temprx [52];}  
                    break  