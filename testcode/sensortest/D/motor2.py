import RPi.GPIO as GPIO
import time

motor2_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor2_pin, GPIO.OUT)

p2 = GPIO.PWM(motor2_pin, 50)

p2.start(0)

cnt = 0

try:

    while True:

	p2.ChangeDutyCycle(10.0)
	time.sleep(1)
	p2.ChangeDutyCycle(11.0)
	time.sleep(1)


except KeyboardInterrupt:
    print("end")
    GPIO.cleanup()
    p2.stop()
