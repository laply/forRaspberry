import sensorGpio
import datetime
import sensorTopic

class Sensor :
	all_pin = [22, 25, 24, 23, 27, 16, 26]
	# dht11_pin = 22 / fire_pin = 25 / led_red_pin = 24 / led_green_pin = 23
	# shock_pin = 27 / ir_sensor_pin = 16 / button_pin = 26


	# dev server IP
	# ipPort = ["124.139.136.86", "1883"]
	# test server IP
	ipPort = ["115.20.144.97", "11183"]

	sending = sensorTopic.SendTopic(ipPort)

	def __init__(self, GPIO, localIP):
		self.localIp = localIP

	def sensing(self):
		self.getData()

	def getData(self):
		if self.sending.getFlag() == "start" :
			self.sendAll(0)
			self.sending.setFlag(".")
		elif self.sending.getFlag() == "get" :
			self.sendAll(1)
			self.sending.setFlag(".")
		elif self.sending.getFlag() == "localIP" :
			self.sendAll(2)
			self.sending.setFlag(".")	

	def sendAll(self, i):
		if i == 0 :
			self.sending.send(0, 0)
			self.sending.send(1, 0)
			self.sending.send(2, 0)
			self.sending.send(3, 0)
			self.sending.send(4, 0)
			self.sending.send(5, self.localIp)
			self.sending.send(6, "send-start")
		elif i == 1:
			self.sending.send(0, 1)
			self.sending.send(1, 2)
			self.sending.send(2, 3)
			self.sending.send(3, 4)
			self.sending.send(4, 5)
			self.sending.send(5, self.localIp)		
			self.sending.send(6, "send-start")
		elif i == 2:
			self.sending.send(5, self.localIp)	
