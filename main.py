import time
from temperature_sensor import read_temperature
from display_controller import lcd
from led_controller import set_color, temperature_to_color
from motion_sensor import motion_sensor
from light_sensor import light_sensor

def main():
    print("Entering main loop")    
    while True:
        try:
            temperature, hum = read_temperature()
            temperature = int(temperature)
            hum = int(hum)
            print(f"Temperature: {temperature}, Humidity: {hum}")

            lcd_string = f"T:{temperature:.1f}C H:{hum:.1f}%"
            lcd.clear()
            lcd.putstr(lcd_string)
            print(f"Displayed on LCD: {lcd_string}")
            
            sensed_motion = motion_sensor.value()
            if sensed_motion:
                print("Motion detected")
            
            sensed_light = light_sensor.value()
            if sensed_light:
                print(f"Light detected: {sensed_light}")
            
            time.sleep(0.5)
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting!")
    main()