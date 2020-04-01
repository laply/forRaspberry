import RPi.GPIO as GPIO
import sensor
import testNoPin # node
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

localGlobalIp = os.popen('curl ifconfig.me').read() ## global ip
# localIp = os.popen('hostname -I').read() ##  local ip
# dev server IP 
# ipPort = ["124.139.136.86", "1883"]  
# test server IP
ipPort = ["115.20.144.97", "11183"]

#local port "8891"
cameraPort = "11092"

cameraCheck = os.system('sh /home/pi/raspstart/mjpg.sh &') ##

# Can Use GPIO
# mainInstance = sensor.Sensor(GPIO, localGlobalIp)

# Can not use GPIO
mainInstance = testNoPin.Sensor(GPIO, localGlobalIp, ipPort, cameraPort)

def startToSensing():
		mainInstance.sensing()

try:
	print("start")
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
