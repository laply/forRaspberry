import RPi.GPIO as gpio
import time
import paho.mqtt.client as mqtt

led_pin1 = 23
led_pin2 = 24
button_pin = 25

client = mqtt.Client()

client.connect("172.30.1.14")
topic = "hi/there"

gpio.setmode(gpio.BCM)
gpio.setup(led_pin1, gpio.OUT)
gpio.setup(led_pin2, gpio.OUT)
gpio.setup(button_pin, gpio.IN)


try:
    print("start")
    client.loop_start()
    client.publish(topic, "start_test_LednBt.py")
    i = 0
    while True:

	if gpio.input(button_pin) == False:
	    i =  i + 1
	    client.publish(topic, "on Clicked Button {}".format(i))
	    print("pin1")
	    gpio.output(led_pin1, True)
	    time.sleep(1)
	    gpio.output(led_pin1, False)
	    time.sleep(0.5)

            print("pin2")
            gpio.output(led_pin2, True)
            time.sleep(1)
            gpio.output(led_pin2, False)
            time.sleep(0.5)


except KeyboardInterrupt:
    client.publish(topic, "end_test_LednBt.py")
    print("end")
    gpio.cleanup()
    client.loop_stop()
    client.disconnect()
