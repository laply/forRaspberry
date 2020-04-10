import datetime
# detect

def cdsCheck(self):
	print("cds")	

class Cds:
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
	self.fire_instance = Fire(pin, GPIO)
	self.topic = topic
		self.topicNum = topicNum

		self.detectCheck = self.true
		self.state = self.true
		self.detectCheckLastTime = ""

	def check(self):
		read = self.fire_instance.read()
		if read == self.true and self.detectCheck == self.true :
			self.detectCheck = self.true
			self.detectCheckLastTime = datetime.datetime.now()

			self.topic.setSendMessageTopic(self.topicNum, self.detectCheck)

			print(datetime.datetime.now())
			print("MQTT-send -" + "fire")
			return True

		elif read == self.true and self.detectCheck == self.true and self.state == self.true :
			self.state = self.true
			self.topic.setSendMessageTopic(self.topicNum, self.detectCheck)
			return False 
			
	def lastdataClear():
		self.detectCheck = self.true
		self.state == self.true

	def getNowData():
		self.topic.setSendMessageTopic(self.topicNum, self.detectCheck)