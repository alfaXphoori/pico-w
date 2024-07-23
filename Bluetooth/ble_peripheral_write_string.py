# This example demonstrates a simple peripheral.

import bluetooth
import random
import struct
import time
import machine
import ubinascii
from ble_advertising import advertising_payload
from micropython import const
from machine import Pin

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_INDICATE_DONE = const(20)

_FLAG_READ = const(0x0002)
_FLAG_NOTIFY = const(0x0010)
_FLAG_INDICATE = const(0x0020)

# org.bluetooth.service.environmental_sensing
_USER_DATA_UUID = bluetooth.UUID(0x181C)
# org.bluetooth.characteristic.temperature
_NAME_UUID = (
    bluetooth.UUID(0x2A8A),
    _FLAG_READ,
)
_USER_DATA_SERVICE = (
    _USER_DATA_UUID,
    (_NAME_UUID,),
)

class BLEUserData:
    def __init__(self, ble, name="PICO-W:Phoori"):
        self._sensor_temp = machine.ADC(4)
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._handle,),) = self._ble.gatts_register_services((_USER_DATA_SERVICE,))
        self._connections = set()
        if len(name) == 0:
            name = 'Pico %s' % ubinascii.hexlify(self._ble.config('mac')[1],':').decode().upper()
        print('Sensor name %s' % name)
        self._payload = advertising_payload(
            name=name, services=[_USER_DATA_UUID]
        )
        self._advertise()

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)

        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_INDICATE_DONE:
            conn_handle, value_handle, status = data
    
    def my_name(self):
        for conn_handle in self._connections:
            name = self._get_name()
            print(name)
            self._ble.gatts_write(self._handle, name,)

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)       
        
    def _get_name(self):
        _name = "Phoori"
        return _name
    
def demo():
    ble = bluetooth.BLE()
    user_d = BLEUserData(ble)
    led = Pin('LED', Pin.OUT)
    counter = 0 
    while True:
        user_d.my_name()
        led.toggle()
        time.sleep_ms(1000)
        counter += 1

if __name__ == "__main__":
    demo()
