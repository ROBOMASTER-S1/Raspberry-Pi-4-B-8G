# My first Raspberry Pi 4 Python program example:

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1
# red LED's = 10
# button = 1
# LCD display = 1
# 220 ohm resistor = 10
# 10K ohm resistor = 1
# some jumper wire

# Note: you may need to watch a future YouTube video
# that will show you how to correctly set up everything
# onto the breadboard.

from time import sleep as wait;import RPi.GPIO as GPIO
import drivers

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins=(7,11,13,15,29,31,33,35,37,12)
position_tuple=(0,2,4,6,8)
display=drivers.Lcd();hz=500

display=drivers.Lcd()
display.lcd_clear()

for i in pins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)
   
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)

print('starting program:')
print('\nPress the Button please!')

display.lcd_display_string(
'PRESS THE BUTTON',1)
display.lcd_display_string(
'PLEASE!',2)

def red_led_flash():
   
    display.lcd_display_string(
    'RED LEDS FLASH:',1)

    for i in range(5):
        for j in range(10):
            GPIO.output(pins[j],GPIO.LOW)
        wait(.1)

        for j in range(10):
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)
       
    for i in pins:
        GPIO.output(i,GPIO.LOW)
    display.lcd_clear()

def red_led_back_forth():
   
    display.lcd_display_string(
    'RED LED',1)
    display.lcd_display_string(
    'BACK/FORTH:',2)

    for i in range(2):
        for j in range(0,9):
            GPIO.output(pins[j],GPIO.HIGH)
            wait(.05)
            GPIO.output(pins[j],GPIO.LOW)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.HIGH)
            wait(.05)
            GPIO.output(pins[j],GPIO.LOW)
           
    display.lcd_clear()
   
def red_led_back_forth_inverse():
   
    display.lcd_display_string(
    'RED LED',1)
    display.lcd_display_string(
    'BACK/FORTH INV:',2)

    for i in range(10):
        GPIO.output(pins[i],GPIO.HIGH)

    for i in range(2):
        for j in range(0,9):
            GPIO.output(pins[j],GPIO.LOW)
            wait(.05)
            GPIO.output(pins[j],GPIO.HIGH)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.LOW)
            wait(.05)
            GPIO.output(pins[j],GPIO.HIGH)

        for j in range(10):
            GPIO.output(pins[j],GPIO.HIGH)
           
    display.lcd_clear()

def red_leds_side_to_side():
   
    display.lcd_display_string(
    'RED LEDS',1)
    display.lcd_display_string(
    'SIDE TO SIDE:',2)

    for i in range(2):
        for j in range(0,10):
            GPIO.output(pins[j],GPIO.HIGH)
            wait(.05)

        for j in range(0,10):
            GPIO.output(pins[j],GPIO.LOW)
            wait(.05)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.HIGH)
            wait(.05)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.LOW)
            wait(.05)
           
    display.lcd_clear()
     
def red_leds_inward_outward():
   
    display.lcd_display_string(
    'RED LEDS',1)
    display.lcd_display_string(
    'INWARD/OUTWARD:',2)

    for i in range(5):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        wait(.1)
       
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        wait(.1)
       
    for i in range(5):
        GPIO.output(pins[4-i],GPIO.HIGH)
        GPIO.output(pins[5+i],GPIO.HIGH)
        wait(.1)

    for i in range(5):
        GPIO.output(pins[4-i],GPIO.LOW)
        GPIO.output(pins[5+i],GPIO.LOW)
        wait(.1)
       
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        wait(.1)
       
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        wait(.1)
       
    for i in range(5):
        GPIO.output(pins[4-i],GPIO.HIGH)
        GPIO.output(pins[5+i],GPIO.HIGH)
        wait(.1)

    for i in range(5):
        GPIO.output(pins[4-i],GPIO.LOW)
        GPIO.output(pins[5+i],GPIO.LOW)
        wait(.1)
       
    display.lcd_clear()

def red_leds_collision():
   
    display.lcd_display_string(
    'RED LEDS',1)
    display.lcd_display_string(
    'COLLISION:',2)

    for i in range(5):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
       
    for i in range(3,-1,-1):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
       
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
       
    for i in range(3,-1,-1):    
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
       
    display.lcd_clear()
   
def red_leds_collision_inverse():
   
    display.lcd_display_string(
    'RED LEDS',1)
    display.lcd_display_string(
    'COLLISION INV:',2)

    for i in pins:
        GPIO.output(i,GPIO.HIGH)

    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
       
    for i in pins:
        GPIO.output(i,GPIO.HIGH)
       
    for i in range(3,-1,-1):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
       
    for i in pins:
        GPIO.output(i,GPIO.HIGH)
       
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
       
    for i in pins:
        GPIO.output(i,GPIO.HIGH)
       
    for i in range(3,-1,-1):    
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
       
    display.lcd_clear()

def red_leds_glitch_right_left():
   
    display.lcd_display_string(
    'RED LEDS GLITCH',1)
    display.lcd_display_string(
    'RIGHT/LEFT:',2)
   
    for i in range(5):
        for j in range(5):
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in range(5):
            GPIO.output(pins[j],GPIO.LOW)
           
        for j in range(5,10):
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in range(5,10):
            GPIO.output(pins[j],GPIO.LOW)
           
    display.lcd_clear()
   
def red_leds_glitch_left_right():
   
    display.lcd_display_string(
    'RED LEDS GLITCH',1)
    display.lcd_display_string(
    'LEFT/RIGHT:',2)
   
    for i in range(5):
        for j in range(5,10):
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in range(5,10):
            GPIO.output(pins[j],GPIO.LOW)
           
        for j in range(5):
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in range(5):
            GPIO.output(pins[j],GPIO.LOW)
           
    display.lcd_clear()
   
def red_leds_follow_left():
   
    display.lcd_display_string(
    'RED LEDS FOLLOW',1)
    display.lcd_display_string(
    'LEFT:',2)
   
    for i in range(7):
        for j in position_tuple:
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in position_tuple:
            GPIO.output(pins[j],GPIO.LOW)

        for j in position_tuple:
            GPIO.output(pins[j+1],GPIO.HIGH)
        wait(.1)

        for j in position_tuple:
            GPIO.output(pins[j+1],GPIO.LOW)
           
    display.lcd_clear()

def red_leds_follow_right():
   
    display.lcd_display_string(
    'RED LEDS FOLLOW',1)
    display.lcd_display_string(
    'RIGHT:',2)
   
    for i in range(7):

        for j in position_tuple:
            GPIO.output(pins[j+1],GPIO.HIGH)
        wait(.1)

        for j in position_tuple:
            GPIO.output(pins[j+1],GPIO.LOW)
           
        for j in position_tuple:
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in position_tuple:
            GPIO.output(pins[j],GPIO.LOW)
           
    display.lcd_clear()

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

    dimmer=(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)
   
    display.lcd_display_string(
    'RED LEDS',1)
    display.lcd_display_string(
    'BREATHE:',2)

    for x in range(2):
        for i in range(0,100,3):
            for j in dimmer:
                j.start(0)
                j.ChangeDutyCycle(i)
                wait(.01)

        for i in range(100,-1,-3):
            for j in dimmer:
                j.start(0)
                j.ChangeDutyCycle(i)
                wait(.01)
               
    display.lcd_clear()
   
functions_tuple=(
    red_leds_breathe,
    red_led_back_forth,
    red_led_back_forth_inverse,
    red_leds_side_to_side,
    red_leds_inward_outward,
    red_leds_collision,
    red_leds_collision_inverse,
    red_leds_glitch_right_left,
    red_leds_glitch_left_right,
    red_leds_follow_left,
    red_leds_follow_right)

try:
    while True:
        if GPIO.input(16)==0:
            display.lcd_clear()
            for i in functions_tuple:
                i();red_led_flash()
               
            display.lcd_display_string(
            'PRESS THE BUTTON',1)
            display.lcd_display_string(
            'PLEASE!',2)
           
except KeyboardInterrupt:
    print('\nStop program Execution/run:')
    print('cleanup/release all GPIO pinouts \
to LOW state.')
    display.lcd_clear()
    display.lcd_backlight(0)
    GPIO.cleanup()
