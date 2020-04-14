import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

gas_pin = 6
led_pin1 = 23
led_pin2 = 24

client = mqtt.Client()

#client.connect("115.20.144.97", "11184", 60)
client.connect("172.30.1.11", 1883, 60)
topic = "hi/there"
flag = ""
chechPoint = [400, 300] # 검출 데이터의 분기점 



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
		if GPIO.input(gas_pin) > chechPoint[0] and flag != "on":
    		GPIO.output(led_pin1, True)
			GPIO.output(led_pin2, False)
			flag = "on"
			client.publish(topic, flag)
			print(flag)
		elif GPIO.input(gas_pin) > chechPoint[0] and flag != "start":
    		GPIO.output(led_pin1, True)
			GPIO.output(led_pin2, False)
			flag = "start"
			client.publish(topic, flag)	
    	elif flag != "off":
			GPIO.output(led_pin1, False)
			GPIO.output(led_pin2, True)
			flag = "off"
			client.publish(topic, flag)
			print(flag)


except KeyboardInterrupt:
    client.publish(topic, "end_gas_Base.py")
    print("end")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
