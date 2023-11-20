import serial
from libs.mqtt import mqtt_eiei 
import json
import random
import time
import os
# Define the serial port and baud rate
serial_port = '/dev/ttyUSB0'   # Change this to your 
baud_rate = 9600  # Set the baud rate used by your ESP32

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)


#@use while true to get value
def init_read_serial():
     mqtt_eiei.init_mqtt()

def read_serial():
    mqtt_eiei.run_mqtt()
    try:
        try:
            line = ser.readline()
            # Remove the non-decodable parts
            line = line.replace(b'\xff', b'')
            # Now decode
            line = line.decode().strip()
        except UnicodeDecodeError:
            print("Received non-text data")
        else:
            print("Received: ", line)
            callback_value(line)
            
            
    except KeyboardInterrupt:
        # Close the serial port when the program is interrupted
        ser.close()
        print("Serial port closed.")

def callback_value(serial_value):
    data = json.loads(serial_value)
    # Check if the key exists in the data
    key_to_monitor = "ssid"  # Change this to the key you want to monitor
    if key_to_monitor in data:
        # print(f"{key_to_monitor}: {data[key_to_monitor]}")
        cmd = 'notepad'
        os.system
        _ssid = data["ssid"]
        _passwd = data["passwd"]
        print(data["ssid"])  # Output: John
        print(data["passwd"])   # Output: 30
        cmd = 'nmcli d wifi connect '+_ssid+' password '+_passwd
        os.system(cmd)
        print("ok-set-wifi")

    else:
        mqtt_eiei.client.publish("usb2ttl/msg", serial_value)
        print(f"{key_to_monitor} not found in the data")

