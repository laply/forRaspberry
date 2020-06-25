import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

# 흰색 : A4 (SDA)
# 녹색 : A5 (SCL)

SDA_pin = 25
SCL_pin = 25

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
	client.publish(topic, "start_test_Base.py")

	while True:
		if GPIO.input(use_pin) == False and flag != "on":
			flag = "on"
			GPIO.output(led_pin1, True)
			GPIO.output(led_pin2, False)
			client.publish(topic, flag)
			print(flag)

		elif flag != "off":
			GPIO.output(led_pin1, False)
			GPIO.output(led_pin2, True)

			flag = "off"
			client.publish(topic, flag)
			print(flag)


except KeyboardInterrupt:
	client.publish(topic, "end_test_Base.py")
	print("end")
	GPIO.cleanup()
	client.loop_stop()
	client.disconnect()
