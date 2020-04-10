class IR:
	def __init__(self, pin, GPIO):
		self.__pin = pin
		self.GPIO = GPIO
		self.setting()

	def setting(self):
		self.GPIO.setup(self.__pin, self.GPIO.IN)

	def read(self):
		return self.GPIO.input(self.__pin)


class Control:

	true = 1
	false = 0

	def __init__(self, pin, GPIO, topic, topicNum):
		self.ir_instance = Fire(pin, GPIO)
		self.topic = topic
		self.topicNum = topicNum

		self.detectCheck = false
		self.state == false
		self.detectCheckLastTime = ""


 	def check(self):
		read = self.ir_instance.read()
		if read == false and self.detectCheck == false :
			self.detectCheck = true
			self.detectCheckLastTime = datetime.datetime.now()

			self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)

			print(str(datetime.datetime.now()))
			print("MQTT-send - " + "detect")
			return True

		elif read == false and self.detectCheck == false and self.state == false :
			self.state = true
			self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)
			return False

	def lastdataClear(self):
		self.detectCheck = false
		self.state == false

	def getNowData(self):
		self.topic.setSendMessageTopic(1, self.topicNum, self.detectCheck)
