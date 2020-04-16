import RPi.GPIO as GPIO
import setting
import sensing
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

cameraLocalIp = os.popen('hostname -I').read() ##  local ip
cameraGlobalIp = os.popen('curl ifconfig.me').read() ## global ipls

if cameraLocalIp == cameraGlobalIp:
	cameraIpPort = [cameraGlobalIp, setting.cameraGlobalport, cameraLocalIp]
else :
	cameraIpPort = [cameraGlobalIp, setting.cameraLocalport, cameraLocalIp]

#cameraCheck = os.system('sh /home/pi/raspstart/mjpg.sh &') ##

allIpPort = [setting.brokerIpPort, cameraIpPort]

# Can Use GPIO
mainInstance = sensing.Sensing(GPIO, allIpPort, setting.raspid, setting.sensordata)

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
