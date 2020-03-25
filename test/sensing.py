import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt

# connect for send DATA
client = mqtt.Client()
client.connect("127.30.1.14")
topic_temp = "tcs/temp"
topic_humid = "tcs/humid"
topic_fire = "tcs/fire"
topic_shork = "tcs/shork"


# pin setting
fire_pin = 25
led_red = 23
led_green = 24
shork_pin = 27

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin
instance = dht11.DHT11(pin = 22)
GPIO.setup(fire_pin, GPIO.IN)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(shork_pin, GPIO.IN)

# etc
tHCount = 0
fireFlag = 0
shockFlag = 0

def tempHumid():
	result = instance.read()
	if result.is_valid():
		global tHCount

		now_time = "Last valid input: " + str(datetime.datetime.now())
		temp = "Temperature: %d C" % result.temperature
		humid = "Humidity: %d %%" % result.humidity

		if(tHCount == 5):
			client.publish(topic_temp, temp)
			client.publish(topic_humid, humid)
			tHCount = 0

		print(now_time)
		print(temp)
		print(humid)

		tHCount += 1

		#gpio.output(trig_pin, False)
		#while gpio.input(echo_pin) == 0:
		#	pulse_start = time.time()

def fireData():
	if GPIO.input(fire_pin) == 1:
		GPIO.output(led_red, True)
		GPIO.output(led_green, False)
		client.publish(topic_fire, 1)
	else :
		GPIO.output(led_green, True)
		GPIO.output(led_red, False)
		global fireFlag
		if(fireFlag == 1000):
			client.publish(topic_fire, 0)
			fireFlag = 0

		fireFlag += 1

def shockData():
    if gpio.input(shock_pin) == 1:
        print("shock")
        gpio.output(led_green_pin, True)
        gpio.output(led_red_pin, False)
		client.publish(topic_shork, 1)
    else :
        print("no shock")
        gpio.output(led_green_pin, False)
        gpio.output(led_red_pin, True)
		
		global shockFlag
		if(shockFlag == 1000):
			client.publish(topic_shork, 0)
			shockFlag = 0

		shockFlag += 1


try:
	client.loop_start()
	while True:
		tempHumid()
		fireData()
		shockData()

except KeyboardInterrupt:
	GPIO.cleanup()
