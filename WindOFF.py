import os
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("topic")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.payload == b'OFF':
        os.system("shutdown -s -t 120")
    elif msg.payload == b'ON':
        os.system("shutdown -a")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('user', password='password')
client.connect("ip", 1883, 60)

client.loop_forever()
