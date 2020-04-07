import RPi.GPIO as GPIO
import sensor
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


localIp = os.popen('hostname -I').read() ##  local ip
localPort = "8891"

raspid = "test1"

localGlobalIp = os.popen('curl ifconfig.me').read() ## global ip
cameraPort = "8891"

if localIp == localGlobalIp:
	cameraIpPort =[localGlobalIp, localPort]
else :
	cameraIpPort = [localGlobalIp , cameraPort]

# dev server IP
# brokerIpPort = ["124.139.136.86", "1883"]

# test server IP
#brokerIpPort = ["115.20.144.97", "11183"]
brokerIpPort =["172.30.1.11", "1883"]

allIpPort = [brokerIpPort, cameraIpPort]

#cameraCheck = os.system('sh /home/pi/raspstart/mjpg.sh &') ##

# Can Use GPIO
mainInstance = sensor.Sensor(GPIO, allIpPort, raspid)

# Can not use GPIO
# mainInstance = testNoPin.Sensor(GPIO, brokerIpPort, cameraIpPort)

def startToSensing():
		mainInstance.sensingStart()

try:
	print("start")
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
