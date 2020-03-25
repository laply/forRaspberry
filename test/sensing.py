import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt

# connect for send DATA
client = mqtt.Client()
client.connect("127.30.1.14")
topic_temp = "tcs/dht11/temp"
topic_humid = "tcs/dht11/humid"

# pin setting 
fire_pin = 25
led_red = 23
led_green = 24

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin
instance = dht11.DHT11(pin = 22)
GPIO.setup(fire_pin, GPIO.IN)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)

# etc 
tempHumidCount = 0 

def tempHumid():
	result = instance.read()
	if result.is_valid():
		tempHumidCount++
		now_time = "Last valid input: " + str(datetime.datetime.now())
		temp = "Temperature: %d C" % result.temperature
		humid = "Humidity: %d %%" % result.humidity

		if(tempHumidCount == 10)
			client.publish(topic_temp, temp)
			client.publish(topic_humid, humid)
			tempHumidCount = 0

		print(now_time)
		print(temp)
		print(humid)

		#gpio.output(trig_pin, False)
		#while gpio.input(echo_pin) == 0:
		#	pulse_start = time.time()

def firedata():
	if GPIO.input(fire_pin) == 1:
		GPIO.output(led_red, True)
		GPIO.output(led_green, False)
	else :
		GPIO.output(led_green, True)
		GPIO.output(led_red, False)

try:
	client.loop_start()
	while True:
		tempHumid()
		firedata()




except KeyboardInterrupt:
	GPIO.cleanup()
