import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, rc):
    print("connected result code " + str(rc))
    client.subscribe("tcs/test/phone")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))

client.connect("115.20.144.97", 11183, 60)

print("start_to_send")
client.loop_start()
client.publish("tcs/test1", "hello")
client.loop_stop()
client.disconnect()
print("end_to_send")



try:
    client.loop_start()
    print("start")
    while True:
        client.publish("tcs/", "hello")

except KeyboardInterrupt:
    client.unsubscribe(["tcs/test/phone"])
    client.loop_stop()
    client.disconnect()
    print("end_to_send")
