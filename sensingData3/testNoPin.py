import sensorGpio
import datetime
import mqtt

class Sensor :
	all_pin = [22, 25, 24, 23, 27, 16, 26]
	# dht11_pin = 22 / fire_pin = 25 / led_red_pin = 24 / led_green_pin = 23
	# shock_pin = 27 / ir_sensor_pin = 16 / button_pin = 26


	# dev server IP
	# ipPort = ["124.139.136.86", "1883"]
	# test server IP
	ipPort = ["115.20.144.97", "11183"]

	sending = mqtt.Connect(ipPort)

	def __init__(self, GPIO):
		self.tHCount = 0

	def sensing(self):
		self.getData()

	def getData(self):
		if self.sending.getFlag() == "start" :
			self.sendAll(0)
			self.sending.setFlag(".")
		elif self.sending.getFlag() == "get" :
			self.sendAll(1)
			self.sending.setFlag(".")

	def sendAll(self, i):
		if i == 0 :
			self.sending.send("temp", 0)
			self.sending.send("humid", 0)
			self.sending.send("fire", 0)
			self.sending.send("shock", 0)
			self.sending.send("ir", 0)
			self.sending.send("test", "send-start")
		elif i == 1:
			self.sending.send("temp", 1)
			self.sending.send("humid", 1)
			self.sending.send("fire", 1)
			self.sending.send("shock", 1)
			self.sending.send("ir", 1)
			self.sending.send("test", "send-get")
