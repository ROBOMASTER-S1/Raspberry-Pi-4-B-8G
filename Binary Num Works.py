import time,RPi.GPIO as GPIO,drivers,threading
from datetime import datetime
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

display=drivers.Lcd() # enable the LCD display
display.lcd_clear() # clear the LCD screen
display.lcd_backlight(1) # Turn on backlight

red_bin_leds=[13,15,19,21,23,29,31,33]

on_off=True,False

for i in range(256):
    display.lcd_display_string(
    f'Binary: {i:b}',1)
    display.lcd_display_string(
    f'Hex: {i:X} Dec: {i:d}',2)
    wait(.5)