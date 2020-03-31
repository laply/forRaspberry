import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

def on_connect(client, userdata, rc):
	print("connected result code " + str(rc))
	client.subscribe("test/phone")

def on_message(client, userdata, msg):
	print("Topic: " + msg.topic + " Message: " + str(msg.payload))


client.on_connect = on_connect
client.on_message = on_message

client.connect("115.20.144.97", 11183, 60)


try:
	client.loop_start()
	print("start")
	client.publish("test/broker","hello")

	while True :
		time.sleep(1)
		print("...")
		client.publish("test/broker", "hi")

except KeyboardInterrupt:
    client.unsubscribe(["test/phone"])
    client.loop_stop()
    client.disconnect()
    print("end_to_send")
