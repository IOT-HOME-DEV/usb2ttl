# python3.6

import random

from paho.mqtt import client as mqtt_client
import random
import time

broker = 'localhost'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'user'
password = 'passwd'
client = mqtt_client.Client(client_id)

def init_mqtt():
    client = connect_mqtt()
    client.loop_start()
    client.loop_stop()
    client.disconnect()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("Connected to broker")
        
        if rc == 0:
            print("Connected to MQTT Broker!")

        else:
            print("Failed to connect, return code %d\n", rc)
    # client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.publish("usb2ttl/msg", "start")
    return client


def run_mqtt():
    try:
        # Check if the client is still connected; if not, it will attempt to reconnect
        if not client.is_connected():
            print("Client is not connected. Attempting to reconnect...")
            client.reconnect()
        # Perform other tasks here if needed
        time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("eiei")