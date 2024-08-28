import tm1637
import machine

display = tm1637.TM1637(clk=machine.Pin(16), dio=machine.Pin(17))
def update_display(temperature):
    display.temperature(temperature)
