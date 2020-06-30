import numpy as np
import datetime
import MCP3208
# detect

class Control:
    
	def __init__(self, pin, topic, topicNum):
		self.sound_instance = MCP3208.MCP3208(pin)
		self.len = 30000
		self.topic = topic
		self.topicNum = topicNum

		self.detectCheck = 0
		self.state = False
		self.detectCheckLastTime = ""
    
	def readSound(self):
		return self.sound_instance.analogRead()

	# conv analog data 
	def dataConvt(self):
		soundList = []

		for i in range(self.len):
			soundList.append(self.readSound())

		fft = np.fft.fft(soundList)/self.len
		fft = fft[range(int(self.len/2))]
		fft_m = abs(fft)
		readfft = []

		for i in range(0, len(fft_m)):
			if fft_m[i] > 0.5:
				print(i, fft_m[i])
				if(6000 < i < 8400):
    					return True

        # 1500 - 2100 :: 6000 - 8400
		return False

	def check(self):
		read = self.dataConvt()
		if read == True and self.detectCheck == False:
			self.detectCheck = 1
			self.detectCheckLastTime = datetime.datetime.now()

			self.topic.setSendMessageTopic(0, self.topicNum, self.detectCheck)

			print(datetime.datetime.now())
			print("MQTT-send -" + "sound")
			return True

		elif read == False and self.detectCheck == False and self.state == False :
			self.state = True
			self.topic.setSendMessageTopic(0, self.topicNum, self.detectCheck)
			return False 

	def lastdataClear(self):
		self.detectCheck = 0
		self.state == False

	def getNowData(self):
		self.topic.setSendMessageTopic(0, self.topicNum, self.detectCheck)