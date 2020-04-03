import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

cds_pin = 24
led_pin1 = 17
led_pin2 = 27
client = mqtt.Client()

client.connect("115.20.144.97", "11183", 60)
topic = "hi/there"
flag = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(cds_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)


try:
    print("start")
    client.loop_start()
    client.publish(topic, "start_test_cds.py")

    while True:
	if GPIO.input(cds_pin) == True:
	    	GPIO.output(led_pin1, True)
		GPIO.output(led_pin2, False)
		if flag != "dark":
			flag = "dark"
			client.publish(topic, flag)
			print(flag)
	else :
		GPIO.output(led_pin1, False)
		GPIO.output(led_pin2, True)
		if flag != "on":
			flag = "on"
			client.publish(topic, flag)
			print(flag)



except KeyboardInterrupt:
    client.publish(topic, "end_test_cds.py")
    print("end")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
