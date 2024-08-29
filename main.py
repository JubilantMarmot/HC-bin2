import time
from temperature_sensor import read_temperature
import display_controller
from led_controller import set_color, temperature_to_color

from motion_sensor import motion_sensor
from light_sensor import light_sensor

def main():
    while True:
        temperature, hum = read_temperature()
        temperature = int(temperature)
        hum = int(hum)

        temperature_to_color(temperature)
        time.sleep(0.5)

        update_display(hum)
        time.sleep(0.5)

        display_controller.lcd_write_string(f"T:{temperature:.1f}C H:{hum:.1f}%")

        sensed_motion = motion_sensor.value()
        if sensed_motion:
            print("Sensed motion!")
        sensed_light = light_sensor.value()
        if sensed_light:
            print(f"Sensed light! {sensed_light}")

if __name__ == "__main__":
    print("Starting!")
    main()