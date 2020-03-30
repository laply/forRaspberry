import sensorGpio
import datetime
import mqtt

class Sensor :
	all_pin = [22, 25, 24, 23, 27, 16, 26]
	# dht11_pin = 22 / fire_pin = 25 / led_red_pin = 24 / led_green_pin = 23
	# shock_pin = 27 / ir_sensor_pin = 16 / button_pin = 26
	getflag = ""

	sending = mqtt.Connect("localhost", getflag)

	dht11_instance = sensorGpio.DHT11(pin = all_pin[0])
	fire_instance = sensorGpio.Fire(pin = all_pin[1])
	shock_instance = sensorGpio.Shock(pin = all_pin[4])
	ir_instance = sensorGpio.IR(pin = all_pin[5])
	led_instance = sensorGpio.LED(pin_G = all_pin[3], pin_R = all_pin[2])
	clear_instance = sensorGpio.Button(pin = all_pin[6])

	def __init__(self):
		self.tHCount = 0 
		self.led_instance.write(1)

	def sensing(self):
		self.tempHumidCheck()
		self.fireCheck()
		self.irCheck()
		self.shockCheck()
		self.clearButton()

	def tempHumidCheck(self):
		result = self.dht11_instance.read()
		if result.is_valid():

			now_time = "Last valid input: " + str(datetime.datetime.now())
			temp = "Temperature: %d C" % result.temperature
			humid = "Humidity: %d %%" % result.humidity

			if(self.tHCount == 5):
				self.sending.send("temp", temp)
				self.sending.send("humid", humid)
				self.tHCount = 0

				print(now_time)
				print(temp)
				print(humid)

				# lastTHTime = now_time
				# lastHumid = humid
				# lastTemo = temp

			self.tHCount += 1

	def fireCheck(self):
		read = self.fire_instance.read()
		if read == 1:
			self.sending.send("fire", 1)
			self.led_instance.write(0)
			print("fire")

	def shockCheck(self):
		read = self.shock_instance.read()
		if read == 1:
			self.sending.send("shock", 1)
			self.led_instance.write(0)
			print("shock")

	def irCheck(self):
		read = self.ir_instance.read()
		if read == 0:
			self.sending.send("ir", 1)
			self.led_instance.write(0)
			print("detect")

	def clearButton(self):
		read = self.clear_instance.read()

		if read == 0 :
			self.sending.send("fire", 1)
			self.sending.send("shock", 1)
			self.sending.send("ir", 1)
			self.sending.send("clear", 1)
			self.led_instance.write(1)

			self.fire_instance.lastFire = "0"
			self.shock_instance.lastShock = "0"
			self.ir_instance.lastIR ="0"
