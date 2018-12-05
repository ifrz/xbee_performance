import paho.mqtt.client as mqtt
import time, json
message_count = 0
time_stamps = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/casa/P0/temp")
    # se subscribe a ese topico y queda a la escucha para
    # medir los timestamp de los envios desde el end device

# The callback for when a PUBLISH message is received from the server.
# cada vez que llega un mensaje del end device a ese topico almacena el timestamp
def on_message(client, userdata, msg):
    global time_stamps
    global message_count
    time_stamps.append(time.time())
    message_count += 1
    print(message_count)
    with open('result.json', 'w') as f:
        f.write(json.dumps(time_stamps, sort_keys=True))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.10.66.200", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
