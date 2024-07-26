import network
import binascii
import time
import machine

ssid = 'CE_STD_2_4G_2' #Replace with your Wifi SSID
password = 'CE@STDKSU' #Replace with your Wifi Password

def connect_wifi():
    i = 0 
    if_config = ["IP", "NETMASK", "GATEWAY", "DNS"]
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi!')
    for i in range(4):
        print("{:<10} {:<20}".format(if_config[i],wlan.ifconfig()[i]))
    
def _start():
    connect_wifi()
        

if __name__ == "__main__":
    try:
        _start()
    except KeyboardInterrupt:
        machine.reset()
        print("Exception")
