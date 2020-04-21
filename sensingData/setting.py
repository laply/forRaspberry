raspid = "test1"

brokerIpPort = ["124.139.136.86", "1883"]

cameraGlobalport = "8891"
cameraLocalport = "8891"

useSensor = [True, 0, 0, 0, 1, 0, True, True, True, 1]
 # dht11 / fire / shock / ir / gas / cds / button / led / motor / pm2008


ButtonUpDown = False
# use ADC [7, 9, 10, 11]

adc_pin = [0]
	# gas_adc_pin = 3

all_pin = [22, 25, 24, 23, 27, 16, 26, 5, 20, 21]
	# dht11_pin = 22 / fire_pin = 25 / led_red_pin = 24 / led_green_pin = 23
	# shock_pin = 27 / ir_sensor_pin = 16 / button_pin = 26
	# cds_pin = 5 / motor_pin_1 = 20 / motor_pin_2 = 21


sensordata = [all_pin, adc_pin, useSensor, ButtonUpDown]

# dev server IP
# brokerIpPort = ["124.139.136.86", "1883"]

# test server IP
#brokerIpPort = ["115.20.144.97", "11183"]

