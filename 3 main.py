from machine import Pin, PWM, ADC, I2C
from time import sleep
import _thread
import ahtx0


led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(22, Pin.OUT)
button1 = Pin(10, Pin.IN, Pin.PULL_DOWN)

conversion_factor = (3.3/65535)
sensor_temp = ADC(4)

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400_000)
sensor = ahtx0.AHT20(i2c)


def aht_temp():
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    print("AHT Temperature: %0.2f C" % temperature+" Humidity: %0.2f %% " %humidity)
    
def cpu_temp():
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27-(reading - 0.706)/0.001721
    print('Cpu-Temperature: {:.2f} C'.format(temperature))

def toggle_led():
    global button1
    global led2
    global led3
    while True:
        state_btn = button1.value()
        if state_btn == 1:
            print('C')
            state_led2 = led2.value()
            state_led3 = led3.value()
            if state_led2 == 0:
                led2.value(1)
                print('2')
            elif state_led2 == 1 and state_led3 == 0:
                led3.value(1)
                print('3')
            elif state_led2 == 1 and state_led3 == 1:
                led2.value(0)
                led3.value(0)
                print('0,0')
        sleep(0.2)
        
def pwm_led():
    global led1
    led_pwm = PWM(led1)
    duty_step = 129
    
    #Set PWM frequency
    frequency = 5000
    led_pwm.freq (frequency)
  
    # Increase the duty cycle gradually
    for duty_cycle in range(0, 65536, duty_step):
        led_pwm.duty_u16(duty_cycle)
        sleep(0.005)
        
    # Decrease the duty cycle gradually
    for duty_cycle in range(65536, 0, -duty_step):
        led_pwm.duty_u16(duty_cycle)
        sleep(0.005)
    sleep(1)

def core0():
    while True:
        pwm_led()
        cpu_temp()
        aht_temp()
try:
    # Start thread core1
    _thread.start_new_thread(toggle_led, ())
    # Start thread core2
    core0()
        
except KeyboardInterrupt:
    print("Keyboard interrupt")


