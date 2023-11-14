import os

def install_prereqs():
	os.system('clear')
	os.system('apt update')
	os.system('clear')
	# os.system('apt install python3 python3-rpi.gpio python3-pip dnsmasq hostapd -y')
	os.system('clear')
	print("Installing paho-mqtt pyserial...")
	print()
	os.system('pip3 install paho-mqtt; pip3 install pyserial')
	os.system('clear')

install_prereqs()