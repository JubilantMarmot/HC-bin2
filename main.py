import time
from temperature_sensor import read_temperature
from display_controller import update_display
from led_controller import set_color, temperature_to_color

def main():
    while True:
        temperature = int(read_temperature())
        update_display(temperature)
        temperature_to_color(temperature)
        time.sleep(0.5)

if __name__ == "__main__":
    print("Starting!")
    main()
