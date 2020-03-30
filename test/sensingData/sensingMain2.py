import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import sensor

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

mainInstance = sensor.Sensor()

def startToSensing():
		mainInstance.sensing()

try:
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()