# Led Binary Beat in Motion
# Python program example:

# Note: be mindful while working with
# electroics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1
# LCD display = 1
# LEDs = 8
# 220 ohm resistor = 8
# jumper wire = 19+2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# Led Binary Beat Python program:

# This Raspberry Pi 4 Python program
# allows users to learn all about how
# binary data_bits work with the 74hc595
# shift register.

# We will use the breadboard method:

# GPIO.setmode(GPIO.BOARD)

# This method is for the GPIO pinouts
# not the GPIO numbers, such as BCM

# You can also use the Broadcom SOC
# Channel method if you prefer:

# GPIO.setmode(GPIO.BCM)
# This allows GPIO numbers, not GPIO
# pinouts, such as the breadboard
# method illustrates in our Python
# program example:

import RPi.GPIO as GPIO,drivers
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

led_speed=.8

data_bit=37
latch=35
clock=33

control_shift=data_bit,latch,clock

for i in control_shift:
    GPIO.setup(i,GPIO.OUT)
    
for j in range(8):            
    bin=f'{i:b}'
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(clock,0)
    GPIO.output(latch,1)

while True:
    try:
        display.lcd_clear()
        for i in range(255,127,-1):
            display.lcd_display_string(
            f'Binary: {255-i:b}',1)
            display.lcd_display_string(
            f'Hex: {255-i:X} Dec: {255-i:d}',2)
            for j in range(8):
                bin=f'{i:b}'
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(clock,0)
            GPIO.output(latch,1)
            wait(led_speed)
            
        for i in range(128,256):
            display.lcd_display_string(
            f'Binary: {i:b}',1)
            display.lcd_display_string(
            f'Hex: {i:X} Dec: {i:d}',2)
            for j in range(8):
                bin=f'{i:b}'
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(clock,0)
            GPIO.output(latch,1)
            wait(led_speed)
        wait(1)
            
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        print('\nStop program Execution/run:')
        print('cleanup/release all GPIO pinouts \
to LOW state.')
        
        for j in range(8):            
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(clock,0)
        GPIO.output(latch,1)
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup()
        break