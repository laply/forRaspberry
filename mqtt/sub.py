import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
    print("connected result code " + str(rc))
    client.subscribe("A/B")


def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_massage


client.connect("172.30.1.14", 1883, 60)

try:
    client.loop_forever()

except KeyboardInterrput:
    print("Finished")
    client.unsubscribe(["A/B"])
    client.disconnect()
