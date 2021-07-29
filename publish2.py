import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_outside")
client.connect(mqttbroker)

while True:
    randNumber = uniform(20.0,21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published tempearture "+ str(randNumber) + "to topic TEMPERATURE")
    time.sleep(1)


