import RPi.GPIO as GPIO
import sensor
import testNoPin # node
import subprocess

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

localIp = subprocess.check_call('hostname -I', shell=True) ## ip

#mainInstance = sensor.Sensor(GPIO, localIP)
mainInstance = testNoPin.Sensor(GPIO, localIp)

def startToSensing():
		mainInstance.sensing()

try:
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
