import machine
import math

BETA = 3950.0
T0 = 298.15

adc = machine.ADC(0)
def read_temperature():
    analog_value = adc.read_u16()
    voltage = analog_value * 3.3 / 65535.0

    celsius = 1 / (math.log(1 / (3.3 / voltage - 1)) / BETA + 1.0 / T0) - 273.15
    return celsius
