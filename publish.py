import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttbroker = "120.232.27.27:8080"
client = mqtt.Client("Temperature_inside")
client.connect(mqttbroker)

while True:
    randNumber = uniform(20.0,21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published tempearture "+ str(randNumber) + "to topic TEMPERATURE")
    time.sleep(1)


