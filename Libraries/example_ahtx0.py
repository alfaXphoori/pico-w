from machine import Pin, I2C
from time import sleep
import ahtx0

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400_000)

def aht_Sensor():
    sensor = ahtx0.AHT20(i2c)
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    print("AHT Temperature: %0.2f C" % temperature+" Humidity: %0.2f %% " %humidity)
    
try:
    while True:
        aht_Sensor()
        sleep(1)
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')







