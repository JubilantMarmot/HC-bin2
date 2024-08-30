from machine import Pin, ADC

x = ADC(Pin(27))
y = ADC(Pin(28))

sel = Pin(13)

def get_joystick():
    xv = int(x.read_u16() * 180 / 65535)
    yv = int(y.read_u16() * 180 / 65535)

    return xv, yv