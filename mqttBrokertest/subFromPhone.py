import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
	print("connected with result code " + str(rc))
	client.subscribe("tcs/phone")


def on_message(client, userdata, msg):
	print("Topic: " + msg.topic + " Message: " + str(msg.payload))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
# client.connect("192.168.0.23", 1883, 60)
client.connect("localhost")

#client.connect("localhost")

try:
	print("start")
	client.loop_forever()
except KeyboardInterrupt:
	print("Finished!")
	client.unsubscribe(["tcs/phone"])
	client.disconnect()
