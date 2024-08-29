import machine

r = machine.Pin(2, machine.Pin.OUT)
g = machine.Pin(1, machine.Pin.OUT)
b = machine.Pin(0, machine.Pin.OUT)
def set_color(red, green, blue):
    r.value(red)
    g.value(green)
    b.value(blue)


def temperature_to_color(temp):
    cold_threshold = -10
    warm_threshold = 30
    
    if temp < cold_threshold:
        set_color(0, 0, 1)
    elif temp < 0:
        if temp < (cold_threshold + 0) / 2:
            blue_intensity = 1
            green_intensity = (temp - cold_threshold) / (0 - cold_threshold)
            set_color(0, green_intensity, blue_intensity)
        else:
            green_intensity = 1
            blue_intensity = (0 - temp) / (0 - cold_threshold)
            set_color(0, green_intensity, blue_intensity)
    elif temp < warm_threshold:
        if temp < (0 + warm_threshold) / 2:
            green_intensity = 1
            red_intensity = (temp - 0) / (warm_threshold - 0)
            set_color(red_intensity, green_intensity, 0)
        else:
            red_intensity = 1
            green_intensity = (warm_threshold - temp) / (warm_threshold - 0)
            set_color(red_intensity, green_intensity, 0)
    else:
        set_color(1, 0, 0)