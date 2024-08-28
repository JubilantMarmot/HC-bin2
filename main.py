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

def read_temperature():
    adc_value = adc.read_u16()
    voltage = adc_value * 3.3 / 65535

    resistor = 10000
    ntc_resistance = resistor * (3.3 / voltage - 1)

    R25 = 10000
    B_coefficient = 3950
    Tref = 298.15

    temperature_kelvin = 1 / (1 / Tref + 1 / B_coefficient * math.log(ntc_resistance / R25))
    temperature_celsius = temperature_kelvin - 273.15

    return temperature_celsius

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

    time.sleep(1)
