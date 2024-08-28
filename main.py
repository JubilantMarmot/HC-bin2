from machine import ADC, Pin
import time
import math

ntc_pin = Pin(26)
adc = ADC(0)

def read_temperature():
    #Source: https://docs.wokwi.com/parts/wokwi-ntc-temperature-sensor
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
    temperature = read_temperature()
    print("Temperature: {:.2f} °C".format(temperature))
    time.sleep(1)
