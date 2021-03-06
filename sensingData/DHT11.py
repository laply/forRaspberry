import time
import datetime
# timer

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

	def __init__(self, pin, GPIO):
		self.GPIO = GPIO
		self.__pin = pin

	def read(self):
		self.GPIO.setup(self.__pin, self.GPIO.OUT)
		self.__send_and_sleep(self.GPIO.HIGH, 0.05)
		self.__send_and_sleep(self.GPIO.LOW, 0.02)
		self.GPIO.setup(self.__pin, self.GPIO.IN, self.GPIO.PUD_UP)

		data = self.__collect_input()
		pull_up_lengths = self.__parse_data_pull_up_lengths(data)

		if len(pull_up_lengths) != 40:
			return DHT11Result(DHT11Result.ERR_MISSING_DATA, 0, 0)

		bits = self.__calculate_bits(pull_up_lengths)
		the_bytes = self.__bits_to_bytes(bits)
		checksum = self.__calculate_checksum(the_bytes)

		if the_bytes[4] != checksum:
			return DHT11Result(DHT11Result.ERR_CRC, 0, 0)

		return DHT11Result(DHT11Result.ERR_NO_ERROR, the_bytes[2], the_bytes[0])

	def __send_and_sleep(self, output, sleep):
		self.GPIO.output(self.__pin, output)
		time.sleep(sleep)

	def __collect_input(self):
		unchanged_count = 0
		max_unchanged_count = 100

		last = -1
		data = []
		while True:
			current = self.GPIO.input(self.__pin)
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
				if current == self.GPIO.LOW:
					state = STATE_INIT_PULL_UP
					continue
				else:
					continue

			if state == STATE_INIT_PULL_UP:
				if current == self.GPIO.HIGH:
					state = STATE_DATA_FIRST_PULL_DOWN
					continue
				else:
					continue

			if state == STATE_DATA_FIRST_PULL_DOWN:
				if current == self.GPIO.LOW:
					state = STATE_DATA_PULL_UP
					continue
				else:
					continue

			if state == STATE_DATA_PULL_UP:
				if current == self.GPIO.HIGH:
					current_length = 0
					state = STATE_DATA_PULL_DOWN
					continue
				else:
					continue

			if state == STATE_DATA_PULL_DOWN:
				if current == self.GPIO.LOW:
					lengths.append(current_length)
					state = STATE_DATA_PULL_UP
					continue
				else:
					continue

		return lengths

	def __calculate_bits(self, pull_up_lengths):

		shortest_pull_up = 1000
		longest_pull_up = 0

		for i in range(0, len(pull_up_lengths)):
			length = pull_up_lengths[i]
			if length < shortest_pull_up:
				shortest_pull_up = length
			if length > longest_pull_up:
				longest_pull_up = length

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

class Control:

	def __init__(self, pin, GPIO, topic, topicNum):
		self.dht11_instance = DHT11(pin, GPIO = GPIO)
		self.topic = topic
		self.tempTopicNum = topicNum[0]
		self.humidTopicNum = topicNum[1]

		self.detectCheckLastTime = ""
		self.lastdata = ["", ""]
		
		self.tHCount = 0

	def check(self):
		result = self.dht11_instance.read()
		if result.is_valid():
			now_time = "Last valid input: " + str(datetime.datetime.now())
			temp = result.temperature
			humid = result.humidity

			self.lastdata[0] = temp
			self.lastdata[1] = humid

			if(self.tHCount == 3):
				self.topic.setSendMessageTopic(0, self.tempTopicNum, temp)
				self.topic.setSendMessageTopic(0, self.humidTopicNum, humid)
				self.tHCount = 0

				print(now_time)
				print("MQTT-send temp - %f" % (temp))
				print("MQTT-send humid -  %f" % (humid))

			self.tHCount += 1

	def getNowData(self):
		self.topic.setSendMessageTopic(0, self.tempTopicNum, self.lastdata[0])
		self.topic.setSendMessageTopic(0, self.humidTopicNum, self.lastdata[1])