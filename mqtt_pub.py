import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

brokerUrl = "95b18c726f0e4dd0a4df08c8be520675.s2.eu.hivemq.cloud"
brokerPort = 8883
brokerUsername = "@lunoifp3"
brokerPassword = ""


# create a set of 2 test messages that will be published at the same time
msgs = [
  {'topic': "lab/temperature", 'payload': "33"}, ("lab/presence", "false", 0, False)
]

# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': brokerUsername, 'password': brokerPassword}
publish.multiple(msgs, hostname=brokerUrl, port=brokerPort, auth=auth,
                 tls=sslSettings, protocol=paho.MQTTv31)