# python3.6

import random

from paho.mqtt import client as mqtt_client
import random
import time

broker = 'iot-a916.local'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'user'
password = 'passwd'
client = mqtt_client.Client(client_id)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("Connected to broker")
        if rc == 0:
            print("Connected to MQTT Broker!")
            check_connect=0
        else:
            print("Failed to connect, return code %d\n", rc)


    # client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def run_mqtt():
    client = connect_mqtt()
    client.loop_start()
    # publish(client)
    client.loop_stop()