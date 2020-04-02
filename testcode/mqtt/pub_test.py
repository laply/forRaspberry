import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("172.30.1.14")

#mqttc.connect("localhost")

print("start_to_send")
client.loop_start()
client.publish("tcs/test1", "hello")
client.loop_stop()
client.disconnect()
print("end_to_send")
