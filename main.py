import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

class publisher1:
    mqttbroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Temperature_inside")
    client.connect(mqttbroker)

    while True:
        randNumber = uniform(20.0, 21.0)
        client.publish("TEMPERATURE", randNumber)
        print("Just published tempearture " + str(randNumber) + "to topic TEMPERATURE")
        time.sleep(1)


class publisher2:
    mqttbroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Temperature_outside")
    client.connect(mqttbroker)

    while True:
        randNumber = uniform(20.0, 21.0)
        client.publish("TEMPERATURE", randNumber)
        print("Just published tempearture " + str(randNumber) + "to topic TEMPERATURE")
        time.sleep(1)

class subscriber:
    def on_message(client, userdata, msg):
        print("Received data " + str(msg.payload.decode("utf-8")))

    mqttbroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("myPhone")
    client.connect(mqttbroker)

    client.loop_start()
    client.subscribe("TEMPERATURE")
    client.on_message = on_message
    time.sleep(30)
    client.loop_stop()