import RPi.GPIO as gpio
import time

led_red_pin = 23
led_green_pin = 24
shock_pin = 27

gpio.setmode(gpio.BCM)
gpio.setup(led_red_pin, gpio.OUT)
gpio.setup(led_green_pin, gpio.OUT)
gpio.setup(shock_pin, gpio.IN)

try :
    while True:

        if gpio.input(shock_pin) == 0:
            gpio.output(led_green_pin, True)
            gpio.output(led_red_pin, False)
        else :
            print("shock")
            gpio.output(led_green_pin, False)
            gpio.output(led_red_pin, True)
	    time.sleep(10)

except KeyboardInterrupt:
	gpio.cleanup()
