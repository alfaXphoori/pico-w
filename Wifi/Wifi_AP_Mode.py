import network
import binascii
import time
import machine

ssid = 'PICO_W:Phoori' 
password = 'CE@STDKSU' 

def connect_wifi():
    i = 0 
    if_config = ["IP", "NETMASK", "GATEWAY", "DNS"]
    led = machine.Pin("LED",machine.Pin.OUT)
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)
    while ap.active() == False:
      pass
    print('Connected to WiFi! AP_MODE')
    for i in range(4):
        print("{:<10} {:<20}".format(if_config[i],ap.ifconfig()[i]))
    
def _start():
    connect_wifi()
        
if __name__ == "__main__":
    try:
        _start()
    except KeyboardInterrupt:
        machine.reset()
        print("Exception")
