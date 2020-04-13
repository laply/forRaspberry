import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

gas_pin = 6
led_pin1 = 17
led_pin2 = 27

client = mqtt.Client()


#client.connect("115.20.144.97", "11184", 60)
client.connect("172.30.1.11", 1883, 60)
topic = "hi/there"
flag = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(gas_pin, GPIO.IN)


try:
    print("start")
    client.loop_start()
    client.publish(topic, "start_gas_Base.py")

    while True:

	print(gas_pin)
	if GPIO.input(gas_pin) == False :
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
    client.publish(topic, "end_gas_Base.py")
    print("end")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
