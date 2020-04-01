import RPi.GPIO as GPIO
import sensor
import testNoPin # node
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


localIp = os.popen('hostname -I').read() ## ip

#cameraCheck = os.system('home/pi/raspstart/mjpg.sh')

# mainInstance = sensor.Sensor(GPIO, localIP)
mainInstance = testNoPin.Sensor(GPIO, localIp)

def startToSensing():
		mainInstance.sensing()

try:
	print("start")
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
