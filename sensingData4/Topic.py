import Connect

class Topic :

    # "raspid/"+"Topic"

    sendTopic = ["tcs/rasp/temp", "tcs/rasp/humid",  "tcs/rasp/fire", "tcs/rasp/shock", 
    "tcs/rasp/ir", "tcs/rasp/clear", "tcs/rasp/localIp", "tcs/rasp/cameraPort",
     "test/rasp/broker"]

    TakeTopic = ["tcs/com", "tcs/phone", "tcs/detectServer"]

    computerMessage = ["start", "get", "ipPort"]
    phoneMessage = ["start", "get", "ipPort"]
    detectServerMessage = ["start", "ipPort", "true", "dStart", "dEnd"]

    MessageList = [computerMessage, phoneMessage, detectServerMessage]


    # topic - id/sendTopic


    flag = False
    topic = ""
    data = ""

    def __init__(self, ipPort, raspid):
        self.raspid = raspid
        self.connect = Connect.Connect(ipPort)
        self.initToSub()

    def setTakeMassageTopic(self, topic):
        self.connect.setSubscribe(self.raspid+"/"+ topic)

    def setSendMessageTopic(self, sensorNum, data):
        self.connect.setPublish(self.raspid + "/" + self.sendTopic[sensorNum], data)

    def initToSub(self):
        print("MQTT-initTosub")
        def on_connect(client, userdata, flags, rc):
            print("MQTT-onConnect - " + str(rc))
            for i in self.TakeTopic :
                self.setTakeMassageTopic(self.raspid + "/" + i)

        def on_message(client, userdata, msg):
            print("MQTT-onMessage")
            self.flag = True
            self.topic = str(msg.topic)
            self.data = str(msg.payload)

        self.connect.setOnConnect(on_connect)
        self.connect.setOnMessage(on_message)
