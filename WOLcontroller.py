import paho.mqtt.client as mqtt
from wakeonlan import send_magic_packet



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.payload == b'1':
        send_magic_packet('mac', ip_address='broadcast')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('user', password='password')
client.connect("ip", 1883, 60)


client.loop_forever()
