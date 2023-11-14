import serial
from libs.mqtt import mqtt_eiei 
# Define the serial port and baud rate
serial_port = '/dev/cu.usbserial-0001'  # Change this to your 
baud_rate = 115200  # Set the baud rate used by your ESP32

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)


#@use while true to get value
def init_read_serial():
     mqtt_eiei.run_mqtt()

def read_serial():
        try:

            line = ser.readline().decode().strip()
    
            print("Received: ", line)
            mqtt_eiei.client.publish("usb2ttl/msg", line)
         
        except KeyboardInterrupt:
            # Close the serial port when the program is interrupted
            ser.close()
            print("Serial port closed.")

