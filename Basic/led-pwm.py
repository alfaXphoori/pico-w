from machine import Pin, PWM
from time import sleep
import _thread

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(22, Pin.OUT)
button1 = Pin(10, Pin.IN, Pin.PULL_DOWN)  

def toggle_led():
    global button1
    global led2
    global led3
    while True:
        led2.value(1)
        led3.value(0)
        sleep(1)
        led2.value(0)
        led3.value(1)
        sleep(1)
        
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
    
def core0():
    while True:
        pwm_led()
        sleep(1)
try:
    # Start thread core1
    _thread.start_new_thread(toggle_led, ())
    # Start thread core2
    core0()
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
