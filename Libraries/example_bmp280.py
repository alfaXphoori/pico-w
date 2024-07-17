from machine import Pin, I2C
from time import sleep
from bmp280 import *

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400_000)

def bmp_Sensor():
    bmp = BMP280(i2c)
    bmp.use_case(BMP280_CASE_INDOOR)
    pressure=bmp.pressure
    altitude=pressure*0.00010199773339984
    temperature=bmp.temperature
    print("Temperature: {} C".format(temperature)+ ", Pressure: {} Pa, Water_level: {} meter".format(pressure,altitude))
    
try:
    while True:
        bmp_Sensor()
        sleep(1)
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')







