import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

motor1_pin = 17
motor2_pin = 27

loc = 8.5
def on_connect(client, userdata, rc):
	client.subscribe("tcs/move")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))
    if msg.topic == "tcs/move" :
        if msg.payload == "plus" :
            loc = loc + 1
        elif msg.payload == "minus":
            loc = loc - 1    
        p1.ChangeDutyCycle(loc)
        
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

mqtt.connect("124.139.136.86", 1883, 60)


GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

p1 = GPIO.PWM(motor1_pin, 50)
p2 = GPIO.PWM(motor2_pin, 50)

p1.start(0)
p2.start(0)

try:
    p1.ChangeDutyCycle(loc)
    client.loop_forever()


except KeyboardInterrupt:
    client.loop_stop()
    print("end")
    GPIO.cleanup()
    p1.stop()
    p2.stop()