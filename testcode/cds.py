import RPi.GPIO as gpio
import time

led_red_pin = 23
led_green_pin = 24
cds_pin = 17

gpio.setmode(gpio.BCM)
gpio.setup(led_red_pin, gpio.OUT)
gpio.setup(led_green_pin, gpio.OUT)
gpio.setup(cds_pin, gpio.IN)

try :
    while True:

        if gpio.input(cds_pin) == 1:
            gpio.output(led_green_pin, True)
            gpio.output(led_red_pin, False)
        else :
            print("dark")
            gpio.output(led_green_pin, False)
            gpio.output(led_red_pin, True)

except KeyboardInterrupt:
	gpio.cleanup()
