import paho.mqtt.client as mqtt

class PubSensor :
    all_topic = ["tcs/temp", "tcs/humid",  "tcs/fire", "tcs/shock", "tcs/ir", "tcs/clear"]
	# topic_temp = "tcs/temp" // topic_humid = "tcs/humid" // topic_fire = "tcs/fire"
	# topic_shock = "tcs/shock" // topic_IR = "tcs/ir" // topic_clear = "tcs/clear"
    
    client = mqtt.Client()
    
    def __init__(self, conIp):
        try:
            self.client.loop_start()
        except KeyboardInterrupt:
            print("Finished-pub")
            self.client.loop_stop()
            self.client.disconnect()

    def send(self, sensorName, data):
        num = 1
        if sensorName == "temp":
            num = 0
        elif sensorName == "humid":
            num = 1
        elif sensorName == "fire":
            num = 2
        elif sensorName == "shock":
            num = 3
        elif sensorName == "ir":
            num = 4
        elif sensorName == "clear":
            num = 5

        self.client.publish(self.all_topic[num], data)

        