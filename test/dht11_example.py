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

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 5
instance = dht11.DHT11(pin = 22)

try:
	client.loop_start()
	while True:
		result = instance.read()
		if result.is_valid():
			now_time = "Last valid input: " + str(datetime.datetime.now())
			temp = "Temperature: %d C" % result.temperature
			humid = "Humidity: %d %%" % result.humidity

			client.publish(topic_temp, temp)
			client.publish(topic_humid, humid)

			print(now_time)
			print(temp)
			print(humid)

		time.sleep(10)

except KeyboardInterrupt:
	GPIO.cleanup()
