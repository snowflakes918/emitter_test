import socket
import emitter
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, msg):
    print("Received data " + str(msg.payload.decode("utf-8")))

mqttbroker = "120.232.27.27:8080"

client = mqtt.Client("myPhone")
print(str(socket.getaddrinfo('120.232.27.27', 8080)))
client.connect(mqttbroker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_stop()


