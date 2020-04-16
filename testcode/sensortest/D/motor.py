import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

motor1_pin = 17
motor2_pin = 27

loc1 = 8.5
loc2 = 8.5

def on_connect(client, userdata, flags, rc):
    print("connect")
    client.subscribe("tcs/rasp/move")

def on_message(client, userdata, msg):
    global loc1
    global loc2   
    if str(msg.topic) == "tcs/rasp/move" :
        if str(msg.payload) == "plus" :
            if loc1 != 12.5:
                loc1 = loc1 + 1
            p1.ChangeDutyCycle(loc1)
        elif str(msg.payload) == "minus":
            if loc1 != 2.5:
                loc1 = loc1 - 1    
            p1.ChangeDutyCycle(loc1)
        elif str(msg.payload) == "up" :
            if loc2 != 12.5:
                loc2 = loc2 + 1
            p2.ChangeDutyCycle(loc2)
        elif str(msg.payload) == "down":
            if loc2 != 2.5:
                loc2 = loc2 - 1    
            p2.ChangeDutyCycle(loc2)

        
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
    p1.ChangeDutyCycle(loc1)
    p2.ChangeDutyCycle(loc2)
    client.loop_forever()


except KeyboardInterrupt:
    client.loop_stop()
    print("end")
    GPIO.cleanup()
    p1.stop()
    p2.stop()