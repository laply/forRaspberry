import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

use_pin = 14

led_pin1 = 23
led_pin2 = 24

client = mqtt.Client()

client.connect("115.20.144.97", "11184", 60)
topic = "hi/there"
flag = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(use_pin, GPIO.IN)

try:
	print("start")
	client.loop_start()
	client.publish(topic, "start_test_temp.py")

	while True:
		print(GPIO.input(use_pin))
		if GPIO.input(use_pin) == False and flag != "on" :
			GPIO.output(led_pin1, True)
			GPIO.output(led_pin2, False)

			flag = "on"
			client.publish(topic, flag)
			print(flag)
		elif GPIO.input(use_pin) == True and flag != "off" :
			GPIO.output(led_pin1, False)
			GPIO.output(led_pin2, True)
			flag = "off"
			client.publish(topic, flag)
			print(flag)


except KeyboardInterrupt:
	client.publish(topic, "end_test_temp.py")
	print("end")
	GPIO.cleanup()
	client.loop_stop()
	client.disconnect()
