import Connect

class SendTopic :
    sendTopic = ["tcs/temp", "tcs/humid",  "tcs/fire", "tcs/shock", "tcs/ir", "tcs/clear", "test/broker"]
	# topic_temp = "tcs/temp" // topic_humid = "tcs/humid" // topic_fire = "tcs/fire"
	# topic_shock = "tcs/shock" // topic_IR = "tcs/ir" // topic_clear = "tcs/clear"
    getTopic = ["tcs/com", "test/phone"]

    Topic = ""
    flag = ""

    def __init__(self, ipPort):
        self.connect = Connect.connect(ipPort)
        self.initToSub()

    def getFlag(self):
	    return self.flag

    def setFlag(self, data):
        self.flag = data

    def send(self, sensorName, data):
        if sensorName == "temp" :
            self.connect.sendPublish(self.sendTopic[0], data)
        elif sensorName == "humid":
            self.connect.sendPublish(self.sendTopic[1], data)
        elif sensorName == "fire":
            self.connect.sendPublish(self.sendTopic[2], data)
        elif sensorName == "shock":
            self.connect.sendPublish(self.sendTopic[3], data)
        elif sensorName == "ir":
            self.connect.sendPublish(self.sendTopic[4], data)
        elif sensorName == "clear":
            self.connect.sendPublish(self.sendTopic[5], data)
        elif sensorName == "test":
            self.connect.sendPublish(self.sendTopic[6], data)

    def initToSub(self):
    	print("MQTT-initTosub")

	def on_connect(client, userdata, flags, rc):
		print("MQTT-onConnect - " + str(rc))
		for i in self.getTopic :
			self.connect.setSubscribe(i)

        def on_message(client, userdata, msg):
    		print("MQTT-onMessage")
	    	self.flag = str(msg.payload)

	self.connect.setOnConnect(on_connect)
	self.connect.setOnMessage(on_message)