#python3
import paho.mqtt.client as mqtt

server = "iot-c16d.local"
port = 1883
keep_alive = 60
username = "user"
password = "password"
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            publish("/c16d/topic/start", "Connected to MQTT Broker")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client("ff123")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(server, port)
    return client

def run_mqtt():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/topic") #subscribe here

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

   
def publish(topic, message):
        client.publish(topic, message)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, port, keep_alive)

client.loop_forever()
