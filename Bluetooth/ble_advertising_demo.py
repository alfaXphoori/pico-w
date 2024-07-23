
import bluetooth
import struct
import time
import ubinascii
from ble_advertising import advertising_payload
from micropython import const
_USER_DATA_UUID = bluetooth.UUID(0x181C) #User Data UUID 

class ble_Advertising:
    def __init__(self, ble, name="Pico_W_BLE"):
        self._ble = ble
        self._ble.active(True)
        if len(name) == 0:
            name = 'Pico %s' % ubinascii.hexlify(self._ble.config('mac')[1],':').decode().upper()
        print('BLE Name: %s  ' % name+ 'Mac: %s' %ubinascii.hexlify(self._ble.config('mac')[1],':').decode().upper())
        self._payload = advertising_payload(name=name, services=[_USER_DATA_UUID],)
        self._advertise()

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)
  
def demo():
    ble = bluetooth.BLE()
    ble_Advertising(ble)

if __name__ == "__main__":
    demo()
