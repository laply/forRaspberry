import datetime
import time
import Topic
import receive

import DHT11
import Shock
import Fire
import IR
import Button
import LED

class Sensing :

	def __init__(self, GPIO, allIpPort, raspid, sensordata):
		self.tHCount = 0
		self.brokerIpPort = allIpPort[0]
		self.cameraIpPort = allIpPort[1]
		self.all_pin = sensordata[0]
		self.useSensor = sensordata[1]
		self.topic = Topic.Topic(self.brokerIpPort, raspid)
		
		self.sensorTimerControl = []
		self.sensorDetectControl = []

		self.setInstance(GPIO)
		self.receive = receive.Receive([self.sensorTimerControl, self.sensorDetectControl], self.cameraIpPort, self.topic)
		self.led_instance.write(1)

	def setInstance(self, GPIO):
		self.sensorTimerControl.append(DHT11.Control(self.all_pin[0], GPIO, self.topic,[0 ,1])) # topic 0 / 0, 1
		self.sensorDetectControl.append(Fire.Control(self.all_pin[1], GPIO, self.topic, 2)) # topic 1 / 0
		self.sensorDetectControl.append(Shock.Control(self.all_pin[4], GPIO, self.topic, 3))  # topic 1 / 1
		self.sensorDetectControl.append(IR.Control(self.all_pin[5], GPIO, self.topic, 4)) #  topic 1 / 2

		# topic 1 / 3 gas
		# topic 1 / 4 cds 
		self.button_instance = Button.Control(self.all_pin[6], GPIO, self.topic)
		self.led_instance = LED.LED(self.all_pin[3], self.all_pin[2], GPIO)

	def sensingStart(self):
		self.sensingList()
		self.receive.getData(self.raspid)

	def sensingList(self):
		while i in self.sensorDetectControl :
			data = i.check()
			if data == True :
				self.led_instance.write(0)
		
		if self.button_instance.clearButton(sensorDetectControl):
			self.led_instance.write(1)