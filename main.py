import serial
from libs.usb2serial import usb2ttl_eiei as usbttl

def main():
    while True:
        usbttl.read_serial()
        

if __name__ == "__main__":
    
    usbttl.init_read_serial()
    main()
