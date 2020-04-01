import RPi.GPIO as GPIO
import sensor
import testNoPin # node 
import subprocess

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

localIp = subprocess.call('hostname -I') ## ip
        
        
#mainInstance = sensor.Sensor(GPIO, localIP)
mainInstance = testNoPin.Sensor(GPIO, localIp)

def startToSensing():
		mainInstance.sensing()

try:
	subprocess.call('') ##  카메라 실행 call 
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()