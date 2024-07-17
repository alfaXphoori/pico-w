from machine import Pin, I2C
from time import sleep

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400_000)

def i2c_Scanner():
    print('Scan i2c bus...')
    devices = i2c.scan()
    if len(devices) == 0:
      print("No i2c device !")
    else:
      print('i2c devices found:',len(devices))
      for device in devices:  
        print("Decimal address: ",device," | Hexa address: ",hex(device))
    
try:
    while True:
        i2c_Scanner()
        sleep(1)
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')







