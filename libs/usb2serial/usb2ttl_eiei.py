import serial
from libs.mqtt import mqtt_eiei 
# Define the serial port and baud rate
serial_port = '/dev/cu.usbserial-539E0035171'  # Change this to your 
baud_rate = 9600  # Set the baud rate used by your ESP32

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)


#@use while true to get value
def init_read_serial():
     mqtt_eiei.run_mqtt()

def read_serial():
        try:
            # Read a line from the serial port
            line = ser.readline().decode().strip()
            # Process the received data
            print("Received: ", line)
            mqtt_eiei.publish("/c16d/topic/serial",line)
        except KeyboardInterrupt:
            # Close the serial port when the program is interrupted
            ser.close()
            print("Serial port closed.")
# try:
#     # while True:
#     #     # Read a line from the serial port
#     #     line = ser.readline().decode().strip()
#     #     # Process the received data
#     #     print("Received: ", line)

# except KeyboardInterrupt:
#     # Close the serial port when the program is interrupted
#     ser.close()
#     print("Serial port closed.")

