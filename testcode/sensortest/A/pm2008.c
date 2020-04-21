unsigned char Send_data[5] = {0x11,0x02,0x0B,0x07, 0xDB}; // 농도읽는명령
unsigned char Receive_Buff[56];                           // data buffer
unsigned long PM1, PM25, PM10;                                     // 농도저장변수 : 각 32bit(8bit*4 = 32)
unsigned long COM_SUCCESS, COM_COUNT;                              // 통신성공/통신시도횟수
unsigned char recv_cnt = 0;
 
void Send_CMD(void)                                        // COMMAND
{
  unsigned char i;
  for(i=0; i<5; i++)
  {
    Serial2.write(Send_data[i]);
    delay(1);      // Don't delete this line !!
  }
}

unsigned char Checksum_cal(void)                          // CHECKSUM 
{
  unsigned char count, SUM=0;
  for(count=0; count<55; count++)
  {
     SUM += Receive_Buff[count];
  }
  return 256-SUM;
}
 
void setup() {
  Serial.begin(9600);
  while (!Serial) ;
  Serial2.begin(9600);
  while (!Serial2);
}
 
void loop() {
  COM_COUNT++;  
  Send_CMD();  // Send Read Command
  
  while(1)
  {
    if(Serial2.available())
    { 
       Receive_Buff[recv_cnt++] = Serial2.read();
      if(recv_cnt ==56){recv_cnt = 0; break;}
    }
    
  } 
  if(Checksum_cal() == Receive_Buff[55])  // CS 확인을 통해 통신 에러 없으면
  {
        COM_SUCCESS++;
        PM1 = (unsigned long)Receive_Buff[3]<<24 | (unsigned long)Receive_Buff[4]<<16 | (unsigned long)Receive_Buff[5]<<8| (unsigned long)Receive_Buff[6];  // 농도계산(시프트)
        PM25 = (unsigned long)Receive_Buff[7]<<24 | (unsigned long)Receive_Buff[8]<<16 | (unsigned long)Receive_Buff[9]<<8| (unsigned long)Receive_Buff[10];  // 농도계산(시프트)
        PM10 = (unsigned long)Receive_Buff[11]<<24 | (unsigned long)Receive_Buff[12]<<16 | (unsigned long)Receive_Buff[13]<<8| (unsigned long)Receive_Buff[14];  // 농도계산(시프트)
        Serial.write("COM count : ");
        Serial.print(COM_SUCCESS);
        Serial.write(" / ");
        Serial.print(COM_COUNT);
        Serial.write("    PM1.0 : ");
        Serial.print(PM1);
        Serial.write("    PM2.5 : ");
        Serial.print(PM25);
        Serial.write("    PM10 : ");
        Serial.println(PM10);
   }
   else
   {
     Serial.write("CHECKSUM Error");
   }
   delay(1000);       //1000ms
    
}
