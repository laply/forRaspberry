import RPi.GPIO as GPIO
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