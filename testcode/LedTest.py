import RPi.GPIO as gpio
import time

led_pin1 = 23
led_pin2 = 24

gpio.setmode(gpio.BCM)
gpio.setup(led_pin1, gpio.OUT)
gpio.setup(led_pin2, gpio.OUT)

print("start")
print("pin1")
gpio.output(led_pin1, True)
time.sleep(1)
gpio.output(led_pin1, False)
time.sleep(0.5)

print("pin2")
gpio.output(led_pin2, True)
time.sleep(1)
gpio.output(led_pin2, False)
time.sleep(0.5)

print("both")
gpio.output(led_pin1, True)
gpio.output(led_pin2, True)
time.sleep(1)
gpio.output(led_pin2, False)
time.sleep(0.5)
gpio.output(led_pin1, False)
time.sleep(0.5)


print("end")
gpio.cleanup()
