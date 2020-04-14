import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

NT_pin = 23
led_pin1 = 17
led_pin2 = 27

client = mqtt.Client()

client.connect("115.20.144.97", "11183", 60)
topic = "hi/there"
flag = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(NT_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
	print("start")
	client.loop_start()
	client.publish(topic, "start_test_NTS.py")

	while True:
		if GPIO.input(NT_pin) == True and flag != "on":
			GPIO.output(led_pin1, True)
			GPIO.output(led_pin2, False)
			flag = "on"
			client.publish(topic, flag)
			print(flag)
		else GPIO.input(NT_pin) == False and flag != "off":
			GPIO.output(led_pin1, False)
			GPIO.output(led_pin2, True)
			flag = "off"
			client.publish(topic, flag)
			print(flag)

except KeyboardInterrupt:
    client.publish(topic, "end_test_NTS.py")
    print("end")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
