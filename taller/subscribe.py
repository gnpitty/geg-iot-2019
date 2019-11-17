#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import datetime
import time

estado=1
host= "localhost"

# This is the Subscriber
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("iot2019/+")

def on_message(client, userdata, msg):
  fecha=  datetime.datetime.now()
  topic = msg.topic
  print(str(fecha)+"   Topic:"+msg.topic+"   Mensaje:"+msg.payload.decode())


#client.disconnect()

client = mqtt.Client()
client.connect(host,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
