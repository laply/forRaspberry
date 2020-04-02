import Connect

class Topic :
    sendTopic = ["tcs/temp", "tcs/humid",  "tcs/fire", "tcs/shock", "tcs/ir", "tcs/clear", "tcs/localip", "tcs/cameraport", "test/broker"]
    TakeTopic = ["tcs/com", "tcs/phone", "tcs/detectServer"]

    computerMessage = ["", ""]
    phoneMessage = ["start", "get", "IpPort"]
    detectServerMessage = ["start", "IpPort", "true", "dStart", "dEnd"] 

    MessageList = [computerMessage, phoneMessage, detectServerMessage]

    flag = False
    topic = ""
    data = ""

    def __init__(self, ipPort):
        self.connect = Connect.Connect(ipPort)
        self.initToSub()

    def setTakeMassageTopic(self, topic):
        self.connect.setSubscribe(topic)
    
    def setSendMessageTopic(self, sensorNum, data):
        self.connect.sendPublish(self.sendTopic[sensorNum], data)
    
    def initToSub(self):
        print("MQTT-initTosub")
        def on_connect(client, userdata, flags, rc):
            print("MQTT-onConnect - " + str(rc))
            for i in self.TakeTopic :
                self.setTakeMassageTopic(i)
        
        def on_message(client, userdata, msg):
            print("MQTT-onMessage")
            self.flag = True
            self.topic = userdata
            self.data = str(msg.payload)
        
        self.connect.setOnConnect(on_connect)
        self.connect.setOnMessage(on_message)
