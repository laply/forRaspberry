import RPi.GPIO as GPIO
import sensor
import testNoPin # node
import subprocess

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

print("....")
localIp = ""
print("check Ip")
while True:
	print("....")
	global localIp
	localIp = subprocess.check_call('hostname -I', shell=True) ## ip
	if localIp != "":
		break

#mainInstance = sensor.Sensor(GPIO, localIP)
mainInstance = testNoPin.Sensor(GPIO, localIp)

def startToSensing():
		mainInstance.sensing()

try:
	print("start")
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
