import RPi.GPIO as GPIO
import time
import datetime
import pub
import sub

class DHT11Result:
	ERR_NO_ERROR = 0
	ERR_MISSING_DATA = 1
	ERR_CRC = 2

	error_code = ERR_NO_ERROR
	temperature = -1
	humidity = -1

	def __init__(self, error_code, temperature, humidity):
		self.error_code = error_code
		self.temperature = temperature
		self.humidity = humidity
		
	def is_valid(self):
		return self.error_code == DHT11Result.ERR_NO_ERROR
class DHT11:
	__pin = 0

	def __init__(self, pin):
		self.__pin = pin
		
	def read(self):
		GPIO.setup(self.__pin, GPIO.OUT)

		# send initial high
		self.__send_and_sleep(GPIO.HIGH, 0.05)

		# pull down to low
		self.__send_and_sleep(GPIO.LOW, 0.02)

		# change to input using pull up
		GPIO.setup(self.__pin, GPIO.IN, GPIO.PUD_UP)
		
		# collect data into an array
		data = self.__collect_input()
		
		# parse lengths of all data pull up periods
		pull_up_lengths = self.__parse_data_pull_up_lengths(data)
		
		# if bit count mismatch, return error (4 byte data + 1 byte checksum)
		if len(pull_up_lengths) != 40:
			return DHT11Result(DHT11Result.ERR_MISSING_DATA, 0, 0)
		
		# calculate bits from lengths of the pull up periods
		bits = self.__calculate_bits(pull_up_lengths)
		
		# we have the bits, calculate bytes
		the_bytes = self.__bits_to_bytes(bits)
		
		# calculate checksum and check
		checksum = self.__calculate_checksum(the_bytes)
		if the_bytes[4] != checksum:
			return DHT11Result(DHT11Result.ERR_CRC, 0, 0)
			
		# ok, we have valid data, return it
		return DHT11Result(DHT11Result.ERR_NO_ERROR, the_bytes[2], the_bytes[0])

	def __send_and_sleep(self, output, sleep):
		GPIO.output(self.__pin, output)
		time.sleep(sleep)
		
	def __collect_input(self):

		# collect the data while unchanged found
		unchanged_count = 0
		
		# this is used to determine where is the end of the data
		max_unchanged_count = 100 

		last = -1
		data = []
		while True:
			current = GPIO.input(self.__pin)
			data.append(current)
			if last != current:
				unchanged_count = 0
				last = current
			else:
				unchanged_count += 1
				if unchanged_count > max_unchanged_count:
					break
		
		return data		

	def __parse_data_pull_up_lengths(self, data):

		STATE_INIT_PULL_DOWN = 1
		STATE_INIT_PULL_UP = 2
		STATE_DATA_FIRST_PULL_DOWN = 3
		STATE_DATA_PULL_UP = 4
		STATE_DATA_PULL_DOWN = 5

		state = STATE_INIT_PULL_DOWN

		lengths = [] # will contain the lengths of data pull up periods
		current_length = 0 # will contain the length of the previous period

		for i in range(len(data)):
			
			current = data[i]
			current_length += 1
				
			if state == STATE_INIT_PULL_DOWN:
				if current == GPIO.LOW:
					# ok, we got the initial pull down
					state = STATE_INIT_PULL_UP
					continue
				else:
					continue
			
			if state == STATE_INIT_PULL_UP:
				if current == GPIO.HIGH:
					# ok, we got the initial pull up
					state = STATE_DATA_FIRST_PULL_DOWN
					continue
				else:
					continue
			
			if state == STATE_DATA_FIRST_PULL_DOWN:
				if current == GPIO.LOW:
					# we have the initial pull down, the next will be the data pull up
					state = STATE_DATA_PULL_UP
					continue
				else:
					continue

			if state == STATE_DATA_PULL_UP:
				if current == GPIO.HIGH:
					# data pulled up, the length of this pull up will determine whether it is 0 or 1
					current_length = 0
					state = STATE_DATA_PULL_DOWN
					continue
				else:
					continue
			
			if state == STATE_DATA_PULL_DOWN:
				if current == GPIO.LOW:			
					# pulled down, we store the length of the previous pull up period
					lengths.append(current_length)
					state = STATE_DATA_PULL_UP				
					continue
				else:
					continue
					
		return lengths
		
	def __calculate_bits(self, pull_up_lengths):

		# find shortest and longest period
		shortest_pull_up = 1000
		longest_pull_up = 0
		
		for i in range(0, len(pull_up_lengths)):
				
			length = pull_up_lengths[i]
			if length < shortest_pull_up:
				shortest_pull_up = length
				
			if length > longest_pull_up:
				longest_pull_up = length
				
		# use the halfway to determine whether the period it is long or short
		halfway = shortest_pull_up + (longest_pull_up - shortest_pull_up) / 2
		
		bits = []
		
		for i in range(0, len(pull_up_lengths)):
			
			bit = False
			if pull_up_lengths[i] > halfway:
				bit = True
				
			bits.append(bit)
		
		return bits
	
	def __bits_to_bytes(self, bits):
		
		the_bytes = []
		byte = 0
		
		for i in range(0, len(bits)):
			
			byte = byte << 1
			if (bits[i]):
				byte = byte | 1
			else:
				byte = byte | 0
			
			if ((i + 1) % 8 == 0):
				the_bytes.append(byte)
				byte = 0
				
		return the_bytes
		
	def __calculate_checksum(self, the_bytes):
		return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255		
class Fire:
	__pin = 0
	lastFire = "0"
	
	def __init__(self, pin):
		self.__pin = pin
		self.setting()

	def setting(self):
		GPIO.setup(self.__pin, GPIO.IN)
	
	def read(self):
		self.lastFire = GPIO.input(self.__pin)
		return self.lastFire		
class Shock:
	__pin = 0
	lastShock = "0"

	def __init__(self, pin):
		self.__pin = pin
		self.setting()

	def setting(self):
		GPIO.setup(self.__pin, GPIO.IN)

	def read(self):
		self.lastShock = GPIO.input(self.__pin)
		return self.lastShock
class IR:
	__pin = 0
	lastIR = "0"

	def __init__(self, pin):
		self.__pin = pin
		self.setting()

	def setting(self):
		GPIO.setup(self.__pin, GPIO.IN)

	def read(self):
		self.lastIR = GPIO.input(self.__pin)
		return self.lastIR
class LED:
	__pin_R = 0 
	__pin_G = 0

	def __init__(self, pin_R, pin_G):
		self.__pin_R = pin_R
		self.__pin_G = pin_G
		self.setting()

	def setting(self):
		GPIO.setup(self.__pin_G, GPIO.OUT)
		GPIO.setup(self.__pin_R, GPIO.OUT)

	def write(self, i):
		if(i == 0):
			GPIO.output(self.__pin_G, False)
			GPIO.output(self.__pin_R, True)
		elif(i == 1):
			GPIO.output(self.__pin_G, True)
			GPIO.output(self.__pin_R, False)
class Button:
	__pin = 0

	def __init__(self, pin):
		self.__pin = pin
		self.setting()
	
	def setting(self):
		GPIO.setup(self.__pin, GPIO.IN)

	def read(self):
		return GPIO.input(self.__pin)

class Sensor :
	tHCount = 0
	all_pin = [22, 25, 24, 23, 27, 16, 26]
	seg = 0
	sending = pub.PubSensor("127.30.1.14")
	getting = sub.SubSensor("localhost") 

	# dht11_pin = 22 / fire_pin = 25 / led_red_pin = 24 / led_green_pin = 23 
	# shock_pin = 27 / ir_sensor_pin = 16 / button_pin = 26
	
	dht11_instance = DHT11(pin = all_pin[0])
	fire_instance = Fire(pin = all_pin[1])
	shock_instance = Shock(pin = all_pin[4])
	ir_instance = IR(pin = all_pin[5])
	led_instance = LED(pin_G = all_pin[3], pin_R = all_pin[2])
	clear_instance = Button(pin = all_pin[6])

	#def __init__(self)

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