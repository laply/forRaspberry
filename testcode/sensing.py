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
topic_shock = "tcs/shock"
topic_IR = "tcs/ir"
topic_clear = "tcs/clear"

# pin setting
fire_pin = 25
led_red_pin = 24
led_green_pin = 23
shock_pin = 27
ir_sensor_pin = 16
button_pin = 26

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin
instance = dht11.DHT11(pin = 22)
GPIO.setup(fire_pin, GPIO.IN)
GPIO.setup(led_green_pin, GPIO.OUT)
GPIO.setup(led_red_pin, GPIO.OUT)
GPIO.setup(shock_pin, GPIO.IN)
GPIO.setup(ir_sensor_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN)

# etc
tHCount = 0
fireFlag = 0
shockFlag = 0
IRFlag = 0

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

def led(i):
	if(i == 0):
		GPIO.output(led_green_pin, False)
		GPIO.output(led_red_pin, True)
	elif(i == 1):
		GPIO.output(led_green_pin, True)
		GPIO.output(led_red_pin, False)

def fireData():
	if GPIO.input(fire_pin) == 1:
		led(0)
		client.publish(topic_fire, 1)

def shockData():
	if GPIO.input(shock_pin) == 1:
		print("shock")
		led(0)
		client.publish(topic_shock, 1)

def IRData():
	if GPIO.input(ir_sensor_pin) == 0 :
		print("detect")
		led(0)
		client.publish(topic_IR, 1)


def clearButton():
	if GPIO.input(button_pin) == 0 :
		client.publish(topic_fire, 0)
		client.publish(topic_shock, 0)
		client.publish(topic_IR, 0)
		client.publish(topic_clear, 1)
		led(1)


try:
	led(1)
	client.loop_start()
	while True:
		tempHumid()
		fireData()
		shockData()
		IRData()
		clearButton()

except KeyboardInterrupt:
	GPIO.cleanup()
