import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

motor1_pin = 17
motor2_pin = 27

loc = 8.5

def on_connect(client, userdata, flags, rc):
    print("connect")
    client.subscribe("tcs/move")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))
    if str(msg.topic) == "tcs/move" :
        print("log 1")
        if str(msg.payload) == "plus" :
            print("log 2")
            loc = loc + 1
        elif str(msg.payload) == "minus":
            print("log 3")
            loc = loc - 1    
        p1.ChangeDutyCycle(loc)
        
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("124.139.136.86", 1883, 60)


GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

p1 = GPIO.PWM(motor1_pin, 50)
p2 = GPIO.PWM(motor2_pin, 50)

p1.start(0)
p2.start(0)

try:
    print("start")
    p1.ChangeDutyCycle(loc)
    client.loop_forever()


except KeyboardInterrupt:
    client.loop_stop()
    print("end")
    GPIO.cleanup()
    p1.stop()
    p2.stop()