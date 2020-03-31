import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("connected result code " + str(rc))
	client.subscribe("test/phone")

def on_message(client, userdata, msg):
	print("Topic: " + msg.topic + " Message: " + str(msg.payload))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("115.20.144.97", 11183, 60)

try:
	client.loop_forever()

except KeyboardInterrupt:
	print("Finished")
	client.unsubscribe(["test/phone"])
	client.disconnect()
