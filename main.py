import time
from temperature_sensor import read_temperature
from display_controller import update_display
from led_controller import set_color, temperature_to_color

from motion_sensor import motion_sensor
from light_sensor import light_sensor

def main():
    while True:
        temperature, hum = read_temperature()
        temperature = int(temperature)
        hum = int(hum)

        update_display(temperature)
        temperature_to_color(temperature)
        time.sleep(0.5)

        update_display(hum)
        time.sleep(0.5)

        sensed_motion = motion_sensor.value()
        if sensed_motion:
            print("Sensed motion!")
        sensed_light = light_sensor.value()
        if sensed_light:
            print("Sensed light!")

if __name__ == "__main__":
    print("Starting!")
    main()