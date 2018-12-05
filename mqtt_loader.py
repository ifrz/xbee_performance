import paho.mqtt.client as mqtt
import time, json
message_count = 0
time_stamps = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/casa/P0/humidity")


client = mqtt.Client()
client.on_connect = on_connect

client.connect("10.10.66.200", 1883, 60)
while(True):
    client.publish('/casa/P0/humidity', payload=10, qos=0, retain=False)
    time.sleep(0.05)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
