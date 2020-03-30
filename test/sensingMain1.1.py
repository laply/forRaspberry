import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt

# send data code 
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
getDataFlag = 0

# save last data 
lastTHTime = "0"
lastHumid = "0"
lastTemp = "0"
lastFire = "0"
lastShock = "0" 
lastIR = "0"


def tempHumid():
	result = instance.read()
	if result.is_valid():
		global tHCount
		global lastHumid
		global lastTemp
		global lastTHTime

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
			lastTHTime = now_time
			lastHumid = humid
			lastTemo = temp

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
		global lastFire
		led(0)
		print("fire")
		client.publish(topic_fire, 1)
		lastFire = "1"	

def shockData():
	if GPIO.input(shock_pin) == 1:
		global lastShock
		print("shock")
		led(0)
		client.publish(topic_shock, 1)
		lastShock = "1"

def IRData():
	if GPIO.input(ir_sensor_pin) == 0 :
		global lastIR
		print("detect")
		led(0)
		client.publish(topic_IR, 1)
		lastIR = "1"


def clearButton():
	if GPIO.input(button_pin) == 0 :
		global lastFire
		global lastShock
		global lastIR
		
		client.publish(topic_fire, 0)
		client.publish(topic_shock, 0)
		client.publish(topic_IR, 0)
		client.publish(topic_clear, 1)
		led(1)

		lastFire = "0"
		lastShock = "0"
		lastIR ="0"

def getData():
	if( )






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
