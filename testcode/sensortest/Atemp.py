import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

Aout_pin = 15
Dout_pin = 14

led_pin1 = 17
led_pin2 = 27

client = mqtt.Client()

client.connect("115.20.144.97", "11184", 60)
topic = "hi/there"
flag = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(Aout_pin, GPIO.IN)
GPIO.setup(Dout_pin, GPIO.IN)

try:
    print("start")
    client.loop_start()
    client.publish(topic, "start_test_temp.py")

    while True:

	#	print(GPIO.input(Aout_pin))
	print(GPIO.input(Dout_pin))



	if GPIO.input(Dout_pin) == False :
		GPIO.output(led_pin1, True)
		GPIO.output(led_pin2, False)

		if flag != "on":
			flag = "on"
			client.publish(topic, flag)
			print(flag)
	else :
		GPIO.output(led_pin1, False)
		GPIO.output(led_pin2, True)

		if flag != "off":
			flag = "off"
			client.publish(topic, flag)
			print(flag)


except KeyboardInterrupt:
    client.publish(topic, "end_test_temp.py")
    print("end")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
