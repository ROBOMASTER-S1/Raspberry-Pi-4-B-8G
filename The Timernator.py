# The Timernator Clock Python Program
# example:

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:
 
# Respberry Pi 4 = 1
# breadboard = 1
# LCD display = 1
# LEDs = 13
# 220 ohm resistor = 13
# jumper wire = 17+2 for the Rasp fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

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

from time import sleep as wait
from datetime import datetime
import RPi.GPIO as GPIO,drivers

# Breadboard Metod:
# Actual GPIO Pinouts

pins=(40,7,11,13,15,29,
36,31,33,35,37,12,38)

hz=500

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

for i in pins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)

def red_leds_breathe():
    
    a0=GPIO.PWM(pins[0],hz)
    a1=GPIO.PWM(pins[1],hz)
    a2=GPIO.PWM(pins[2],hz)
    a3=GPIO.PWM(pins[3],hz)
    a4=GPIO.PWM(pins[4],hz)
    a5=GPIO.PWM(pins[5],hz)
    a6=GPIO.PWM(pins[6],hz)
    a7=GPIO.PWM(pins[7],hz)
    a8=GPIO.PWM(pins[8],hz)
    a9=GPIO.PWM(pins[9],hz)
    a10=GPIO.PWM(pins[10],hz)
    a11=GPIO.PWM(pins[11],hz)
    a12=GPIO.PWM(pins[12],hz)

    dimmer=(a0,a1,a2,a3,a4,a5,
    a6,a7,a8,a9,a10,a11,a12)
        
    for i in range(0,100,5):
        for j in dimmer:
            j.start(0)
            j.ChangeDutyCycle(i)
            wait(.01)

    for i in range(100,-1,-5):
        for j in dimmer:
            j.start(0)
            j.ChangeDutyCycle(i)
            wait(.01)
              
while True:
    try:
        display.lcd_display_string(
        ' THE TIMERNATOR', 1)
        display.lcd_display_string(
        str(datetime.now()), 2)
        red_leds_breathe() # call the function
        
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        print('\nStop program Execution/run:')
        print('cleanup/release all GPIO pinouts \
to LOW state.')
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup()
        break  
