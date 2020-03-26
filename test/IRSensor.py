import RPi.GPIO as GPIO
import time 

s_led_red_pin = 21
s_led_green_pin = 20
ir_sensor_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(s_led_red_pin, GPIO.OUT)
GPIO.setup(s_led_green_pin, GPIO.OUT)
GPIO.setup(ir_sensor_pin, GPIO.IN)

try :
    while True :
        if GPIO.input(ir_sensor_pin) == 0:
	    print("out")
            GPIO.output(s_led_red_pin, True)



except KeyboardInterrupt :
    GPIO.cleanup()
