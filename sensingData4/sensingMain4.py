import RPi.GPIO as GPIO
import sensor
import testNoPin # node
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

localGlobalIp = os.popen('curl ifconfig.me').read() ## global ip
cameraPort = "11092"
# localIp = os.popen('hostname -I').read() ##  local ip
# dev server IP 
# brokerIppPort = ["124.139.136.86", "1883"]  
# test server IP
brokerIpPort = ["115.20.144.97", "11183"]

#local port "8891"

cameraCheck = os.system('sh /home/pi/raspstart/mjpg.sh &') ##

cameraIpPort = [ localGlobalIp , cameraPort ]
# Can Use GPIO
# mainInstance = sensor.Sensor(GPIO, localGlobalIp)

# Can not use GPIO
mainInstance = testNoPin.Sensor(GPIO, brokerIpPort, cameraIpPort)

def startToSensing():
		mainInstance.sensingStart()

try:
	print("start")
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
