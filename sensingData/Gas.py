import datetime
import mcp3208
# detect

class Control:

	self.AnalogSensing = mcp3208.MCP3028()

	def __init__(self, pin, GPIO, topic, topicNum):
		self.gas_instance = mcp3208(pin)
		self.topic = topic
		self.topicNum = topicNum

		self.detectCheck = False
		self.state = False
		self.detectCheckLastTime = ""

	# conv analog data 
	def dataConvt(self):
		read = self.fire_instance.read()
		return read

	def check(self):
		read = dataConvt()

		if read == True and self.detectCheck == False:
			self.detectCheck = True
			self.detectCheckLastTime = datetime.datetime.now()

			self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)

			print(datetime.datetime.now())
			print("MQTT-send -" + "gas")
			return True

		elif read == False and self.detectCheck == False and self.state == False :
			self.state = True
			self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)
			return False 

	def lastdataClear(self):
		self.detectCheck = False
		self.state == False

	def getNowData(self):
		self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)