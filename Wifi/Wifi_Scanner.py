import network
import binascii
import time

wlan = network.WLAN() #  network.WLAN(network.STA_IF)

def wifi_scanner(time_delay):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()

    print("{} networks found:\n".format(len(networks)))
    print ("{:<20} {:<20} {:<9} {:<7}".format('SSID', 'MAC ADDRESS', 'CHANNEL', 'RSSI'))
    for net in networks:
        print ("{:<20} {:<20} {:<9} {:<7} ".format(net[0].decode(), binascii.hexlify(net[1]).decode(), net[2], net[3]))
        time.sleep(time_delay)
    
def _start():
    while True:
        wifi_scanner(3) #seconds
        
if __name__ == "__main__":
    try:
        _start()
    except:
        print("Exception")
