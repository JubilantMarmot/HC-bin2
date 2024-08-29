import machine
import time
from machine import Pin, ADC, I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = 0x27

LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETDDRAMADDR = 0x80

def lcd_write(value, mode):
    """Send a command or data to the LCD"""
    i2c.writeto(I2C_ADDR, bytearray([mode, value]))

def lcd_send_command(cmd):
    """Send a command to the LCD"""
    lcd_write(cmd, 0x00)  # 0x00 for command

def lcd_send_data(data):
    """Send data to the LCD"""
    lcd_write(data, 0x40)  # 0x40 for data

def lcd_init():
    """Initialize the LCD"""
    time.sleep_ms(50)
    lcd_send_command(LCD_FUNCTIONSET | 0x10)  # Function set: 4-bit mode
    lcd_send_command(LCD_DISPLAYCONTROL | 0x04)  # Display control
    lcd_send_command(LCD_ENTRYMODESET | 0x02)  # Entry mode

def lcd_clear():
    """Clear the LCD display"""
    lcd_send_command(LCD_CLEARDISPLAY)
    time.sleep_ms(2)  # Delay for clearing

def lcd_set_cursor(row, col):
    """Set the cursor to a specific location"""
    if row == 0:
        address = 0x80 + col
    elif row == 1:
        address = 0xC0 + col
    lcd_send_command(LCD_SETDDRAMADDR | address)

def lcd_write_string(message):
    """Write a string to the LCD"""
    for char in message:
        lcd_send_data(ord(char))

# Initialize LCD
lcd_init()
