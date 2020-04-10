class Receive:   

	def __init__(self, sensorControl, cameraIpPort, topic):
		self.sensorControl = sensorControl
		self.cameraIpPort = cameraIpPort
		self.topic = topic

	def getData(self, raspid):
		if self.topic.flag == True:
			print("take Topic")
			self.topic.flag = False

			if raspid == self.topic.topic[0:len(raspid)] :
				topic = self.topic.topic[len(raspid) + 1:]
			else :
				topic = ""

			for i, sender in enumerate(self.topic.TakeTopic):
				print(topic, i, sender)
				if topic == sender:
					senderData = self.matchingTopic(i)
					print(senderData)
					self.sender(senderData)
					break

	def matchingTopic(self, messgeSenderindex):
		print("start matching Topic")
		data = self.topic.data
		for messageNum, message in enumerate(self.topic.MessageList[messgeSenderindex]):
			print(data, messgeSenderindex, messageNum,  message)
			if data == message :
				return [messgeSenderindex, messageNum]

	def sender(self, senderData):
		print("sender Topic")
		if senderData[0] == 0 :
			self.senderIsCom(senderData[1])
		elif senderData[0] == 1:
			self.senderIsPhone(senderData[1])
		elif senderData[0] == 2:
			self.senderIsDServer(senderData[1])

	def senderIsCom(self, senderMesaage):
		print("sender is com")
		if senderMesaage == 0:
			for i, sensorTimerControl in enumerate(self.sensorControl[0]):
				self.topic.setSendMessageTopic(0, 2*i, sensorTimerControl.lastdata[0])
				self.topic.setSendMessageTopic(0, 2*i + 1, sensorTimerControl.lastdata[1])
			
			for i, sensorDetectControl in enumerate(self.sensorControl[1]):
				self.topic.setSendMessageTopic(1, i, sensorTimerControl.detectCheck)

			for i, cameraIpPortInfo in enumerate(self.cameraIpPort):
				self.topic.setSendMessageTopic(2, i, self.cameraIpPortInfo[i])

		elif senderMesaage == 1:
			for i, sensorTimerControl in enumerate(self.sensorControl[0]):
				self.topic.setSendMessageTopic(0, 2*i, sensorTimerControl.lastdata[0])
				self.topic.setSendMessageTopic(0, 2*i + 1, sensorTimerControl.lastdata[1])
			
			for i, sensorDetectControl in enumerate(self.sensorControl[1]):
				self.topic.setSendMessageTopic(1, i, sensorTimerControl.detectCheck)
			
		elif senderMesaage == 2:
			for i, cameraIpPortInfo in enumerate(self.cameraIpPort):
				self.topic.setSendMessageTopic(2, i, self.cameraIpPortInfo[i])

	# phoneMessage = ["start", "get", "IpPort"]
	def senderIsPhone(self, senderMesaage):
		print("sender is phone")
		if senderMesaage == 0:
			for i, sensorTimerControl in enumerate(self.sensorControl[0]):
				self.topic.setSendMessageTopic(0, 2*i, sensorTimerControl.lastdata[0])
				self.topic.setSendMessageTopic(0, 2*i + 1, sensorTimerControl.lastdata[1])
			
			for i, sensorDetectControl in enumerate(self.sensorControl[1]):
				self.topic.setSendMessageTopic(1, i, sensorTimerControl.detectCheck)

			for i, cameraIpPortInfo in enumerate(self.cameraIpPort):
				self.topic.setSendMessageTopic(2, i, self.cameraIpPortInfo[i])

		elif senderMesaage == 1:
			for i, sensorTimerControl in enumerate(self.sensorControl[0]):
				self.topic.setSendMessageTopic(0, 2*i, sensorTimerControl.lastdata[0])
				self.topic.setSendMessageTopic(0, 2*i + 1, sensorTimerControl.lastdata[1])
			
			for i, sensorDetectControl in enumerate(self.sensorControl[1]):
				self.topic.setSendMessageTopic(1, i, sensorTimerControl.detectCheck)
			
		elif senderMesaage == 2:
			for i, cameraIpPortInfo in enumerate(self.cameraIpPort):
				self.topic.setSendMessageTopic(2, i, self.cameraIpPortInfo[i])

	# detectServerMessage = ["start", "IpPort", "true", "dStart", "dEnd"]
	def senderIsDServer(self, senderMesaage):
		print("sender is DServer")			
		if senderMesaage == 0:
			for i, sensorDetectControl in enumerate(self.sensorControl[1]):
				self.topic.setSendMessageTopic(1, i, sensorTimerControl.detectCheck)
		elif senderMesaage == 1:
			for i, sensorDetectControl in enumerate(self.sensorControl[1]):
				self.topic.setSendMessageTopic(1, i, sensorTimerControl.detectCheck)
