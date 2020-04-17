import datetime
import mcp3208
# detect


class Control:
	true = 1
	false = 0

	self.AnalogSensing = mcp3208.MCP3028()

	def __init__(self, pin, GPIO, topic, topicNum):
		self.fire_instance = Gas(pin, GPIO)
		self.topic = topic
		self.topicNum = topicNum

		self.detectCheck = self.false
		self.state = self.false
		self.detectCheckLastTime = ""

	def check(self):
		read = self.fire_instance.read()
		if read == self.true and self.detectCheck == self.false :
			self.detectCheck = self.true
			self.detectCheckLastTime = datetime.datetime.now()

			self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)

			print(datetime.datetime.now())
			print("MQTT-send -" + "fire")
			return True

		elif read == self.false and self.detectCheck == self.false and self.state == self.false :
			self.state = self.true
			self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)
			return False 

	def lastdataClear(self):
		self.detectCheck = self.false
		self.state == self.false

	def getNowData(self):
		self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)