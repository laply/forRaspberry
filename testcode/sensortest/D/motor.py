import RPi.GPIO as GPIO
import time

motor1_pin = 17
motor2_pin = 27
led_pin1 = 23
led_pin2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

p1 = GPIO.PWM(motor1_pin, 50)  #PMW:펄스 폭 변조
p2 = GPIO.PWM(motor2_pin, 50)  #PMW:펄스 폭 변조
p1.start(0)
p2.start(0)
cnt = 0
try:

    while True:
        p1.ChangeDutyCycle(12.5) #최댓값
        time.sleep(1)
        p1.ChangeDutyCycle(10.0)
        time.sleep(1)
        p1.ChangeDutyCycle(7.5) #0
        time.sleep(1)
        p1.ChangeDutyCycle(5.0)
        time.sleep(1)
        p1.ChangeDutyCycle(2.5) #최솟값
        time.sleep(1)

except KeyboardInterrupt:
    print("end")
    GPIO.cleanup()
    p1.stop()
    p2.stop()