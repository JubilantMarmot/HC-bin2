from machine import ADC, Pin
import time
import math
import tm1637

ntc_pin = Pin(26)
adc = ADC(0)

display = tm1637.TM1637(clk=machine.Pin(16), dio=machine.Pin(17))

r = Pin(2, Pin.OUT)
g = Pin(1, Pin.OUT)
b = Pin(0, Pin.OUT)

def set_color(red, green, blue):
    r.value(red)
    g.value(green)
    b.value(blue)

BETA = 3950.0 #Found these values online after debugging
T0 = 298.15

def read_temperature():
    analog_value = adc.read_u16()
    voltage = analog_value * 3.3

    celsius = 1 / (math.log(1 / (3.3 / voltage - 1)) / BETA + 1.0 / T0) - 273.15
    return celsius

while True:
    temperature = int(read_temperature())
    display.temperature(temperature)

    if temperature < 30:
        set_color(0, 1, 0)
    elif temperature < 29:
        set_color(1, 1, 0)
    elif temperature < 40:
        set_color(1, 0, 0)
    else:
        set_color(1, 0, 0)

    time.sleep(0.5)
