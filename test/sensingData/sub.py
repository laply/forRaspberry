import paho.mqtt.client as mqtt

class SubSensor :
    client = mqtt.Client()
    topic = ["tcs/com", "tcs/phone"]

    def __init__(self, ip):
        self.client.connect(ip, 1883, 60)
        self.subTopic()
        self.client.on_message = self.on_message

        try:
           self.client.loop_forever()
        except KeyboardInterrupt:
            print("Finished-sub")
            self.client.unsubscribe(self.topic)
            self.client.disconnect()

    def subTopic(self):
        for i in self.topic :
            self.client.subscribe(i)

    def on_message(self, client, userdata, msg):
        print("Topic: " + msg.topic + " Message: " + str(msg.payload))

        if msg.topic == self.topic[1] :
            if str(msg.payload) == "start" :
                a = 1
