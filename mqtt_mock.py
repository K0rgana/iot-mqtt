import time
import paho.mqtt.client as paho
from paho import mqtt

import random
import time

brokerUrl = "95b18c726f0e4dd0a4df08c8be520675.s2.eu.hivemq.cloud"
brokerPort = 8883
brokerUsername = "@lunoifp3"
brokerPassword = ""

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(brokerUsername, brokerPassword)
client.connect(brokerUrl, brokerPort)

def mock_number(min, max): 
  return random.randrange(min,max)

def mock_presence(): 
  list = [1, 0]
  return random.choice(list)

def mock_topic(): 
  list = ['temperature', 'presence']
  return random.choice(list)

def mock_msgs(max):
  i=0
  payload = []
  while (i<max):
      topic = mock_topic()
      if topic == 'temperature':
        temp = mock_number(17, 30)  
        msg = {'topic':'lab/temperature', 'payload': temp}
      if topic == 'presence':
        presc = mock_presence()  
        msg = {'topic':'lab/presence', 'payload': presc}
      payload.append(msg)
      i=i+1
  return payload

ttl = mock_number(5, 15)
msgs = mock_msgs(ttl)
for el in msgs:
  time.sleep(5)
  #client.publish("lab/temperature", payload="21", qos=1, retain=True)
  client.publish(el["topic"], payload=el["payload"], qos=1, retain=True)
  print(el)
