
# raspid + "/" + Topic
# topic - id/sendTopic

sensorTimerTopic = ["tcs/rasp/temp", "tcs/rasp/humid"]
sensorDetectTopic = ["tcs/rasp/fire", "tcs/rasp/shock", "tcs/rasp/ir", "tcs/rasp/gas", "tcs/rasp/cds"]

IpPortTopic = ["tcs/rasp/localIp", "tcs/rasp/cameraPort", "tcs/rasp/localIpUnder"]

sendTopic = [sensorTimerTopic, sensorDetectTopic, IpPortTopic]


TakeTopic = ["tcs/com", "tcs/phone", "tcs/detectServer"]

computerMessage = ["start", "get", "ipPort"]
phoneMessage = ["start", "get", "ipPort"]
detectServerMessage = ["start", "ipPort", "true", "dStart", "dEnd"]


MessageList = [computerMessage, phoneMessage, detectServerMessage]