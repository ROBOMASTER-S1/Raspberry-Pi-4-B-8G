# My first Raspberry Pi 4 Python program
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
# button = 1
# LED's = 12
# 220 ohm resistor = 12
# 10K ohm resistor = 1
# jumper wire = 17+2 for the Rasp fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# Note: you may need to watch a future
# YouTube video that will show you how
# to correctly set up everything onto
# the breadboard. However, I do have a
# really cool, three minute video of what
# I created with the Raspberry Pi 4 along
# with Python. Here is the exact Python
# code for making the Raspberry Pi 4 do
# what it can do. As shown in the YouTube
# video example.

# Youtube video link:
# https://www.youtube.com/watch?v=SotulsGjNFE

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
import RPi.GPIO as GPIO,drivers,random

# Breadboard Metod:
# Actual GPIO Pinouts

pins=(7,11,13,15,29,31,33,35,37,12)

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

# led position tuples:

led_position_tuple_1=(0,2,4,6,8) 
led_position_tuple_2=(0,1,4,5,8,9)
led_position_tuple_3=(2,6,3,7)
display=drivers.Lcd();hz=500

GPIO.setup(36,GPIO.OUT) # for blue led
GPIO.setup(38,GPIO.OUT) # for yellow led

# setup the button, while invoking the built-in
# Raspberry Pi 4 resistor for safe protection
# along with a 10K resistor for added protection.

GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.output(36,GPIO.LOW)
for i in pins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW) # all pins are off
    
GPIO.output(38,GPIO.HIGH) # yellow led is on

# Start creating text with the LCD display

display.lcd_display_string(
'GREETINGS HUMAN!',1)

wait(2.5)
display.lcd_clear()

display.lcd_display_string(
'MY NAME IS...',1)
wait(1)
display.lcd_display_string(
'RASPBERRY PI 4.',2)

wait(2.5)
display.lcd_clear()

display.lcd_display_string(
'I AM THE WORLD\'S',1)
display.lcd_display_string(
'SMALLEST PC.',2)

wait(2.5)
display.lcd_clear()

display.lcd_display_string(
'I AM ROCKING:',1)
wait(1)
display.lcd_display_string(
'8GB OF RAM',2)

wait(2.5)
display.lcd_clear()

display.lcd_display_string(
'I AM ROCKING:',1)
display.lcd_display_string(
'32GB SANDISK',2)

wait(2.5)
display.lcd_clear()

display.lcd_display_string(
'I AM ROCKING:',1)
display.lcd_display_string(
'WIFI/BLUETOOTH',2)
wait(2.5)

display.lcd_clear()

display.lcd_display_string(
'LET\'S SHRED SOME',1)
display.lcd_display_string(
'RED LEDS UP!!',2)
wait(2.5)

# Waning Message

display.lcd_clear()
print('\n\nPLEASE NOTE: THE RASPBERRY \
PI IS NOT FOR THE TIMID!') 
print('\nTHE RASPBERRY PI CAN BREAK IF \
YOU IGNORE ANY RULES\nIN BASIC ELECTRONICS. \
BASIC ELECTRONICS DEMANDS BASIC\nMATH SKILLS \
AND KNOWLEDGE OF BASIC ELECTRONIC COMPONENTS \
ALIKE.')

print('\nSTARTING PROGRAM:')
print('\nALRIGHT! LET\'S ROCK!!')
print('\nPRESS THE BUTTON PLEASE!')

display.lcd_display_string(
'PRESS THE BUTTON',1)
display.lcd_display_string(
'PLEASE!',2)

# Have some fun creating your functions

def red_led_flash():
    
    display.lcd_display_string(
    'RED LEDS FLASH:',1)

    for i in range(5):
        for j in range(10):
            GPIO.output(pins[j],GPIO.LOW)
            GPIO.output(36,GPIO.HIGH)
        wait(.1)

        for j in range(10):
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.LOW)
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
            GPIO.output(36,GPIO.HIGH)
            wait(.05)
            GPIO.output(pins[j],GPIO.LOW)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.LOW)
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
            GPIO.output(36,GPIO.LOW)
            wait(.05)
            GPIO.output(pins[j],GPIO.HIGH)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.LOW)
            GPIO.output(36,GPIO.HIGH)
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
            GPIO.output(36,GPIO.HIGH)
            wait(.05)

        for j in range(0,10):
            GPIO.output(pins[j],GPIO.LOW)
            GPIO.output(36,GPIO.LOW)
            wait(.05)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.HIGH)
            wait(.05)

        for j in range(9,-1,-1):
            GPIO.output(pins[j],GPIO.LOW)
            GPIO.output(36,GPIO.LOW)
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
        GPIO.output(36,GPIO.LOW)
        wait(.1)
        
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        GPIO.output(36,GPIO.HIGH)
        wait(.1)
        
    for i in range(5):
        GPIO.output(pins[4-i],GPIO.HIGH)
        GPIO.output(pins[5+i],GPIO.HIGH)
        GPIO.output(36,GPIO.LOW)
        wait(.1)

    for i in range(5):
        GPIO.output(pins[4-i],GPIO.LOW)
        GPIO.output(pins[5+i],GPIO.LOW)
        GPIO.output(36,GPIO.HIGH)
        wait(.1)
        
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        GPIO.output(36,GPIO.LOW)
        wait(.1)
        
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        GPIO.output(36,GPIO.HIGH)
        wait(.1)
        
    for i in range(5):
        GPIO.output(pins[4-i],GPIO.HIGH)
        GPIO.output(pins[5+i],GPIO.HIGH)
        GPIO.output(36,GPIO.LOW)
        wait(.1)

    for i in range(5):
        GPIO.output(pins[4-i],GPIO.LOW)
        GPIO.output(pins[5+i],GPIO.LOW)
        GPIO.output(36,GPIO.HIGH)
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
        GPIO.output(36,GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        
    for i in range(3,-1,-1):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        GPIO.output(36,GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        GPIO.output(36,GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        
    for i in range(3,-1,-1):    
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        GPIO.output(36,GPIO.LOW)
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
        GPIO.output(36,GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        
    for i in pins:
        GPIO.output(i,GPIO.HIGH)
        
    for i in range(3,-1,-1):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        GPIO.output(36,GPIO.HIGH)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        
    for i in pins:
        GPIO.output(i,GPIO.HIGH)
        
    for i in range(5):
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        GPIO.output(36,GPIO.LOW)
        wait(.1)
        GPIO.output(pins[0+i],GPIO.HIGH)
        GPIO.output(pins[9-i],GPIO.HIGH)
        
    for i in pins:
        GPIO.output(i,GPIO.HIGH)
        
    for i in range(3,-1,-1):    
        GPIO.output(pins[0+i],GPIO.LOW)
        GPIO.output(pins[9-i],GPIO.LOW)
        GPIO.output(36,GPIO.HIGH)
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
            GPIO.output(36,GPIO.HIGH)
        wait(.1)

        for j in range(5):
            GPIO.output(pins[j],GPIO.LOW)
            
        for j in range(5,10):
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.LOW)
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
            GPIO.output(36,GPIO.HIGH)
        wait(.1)

        for j in range(5,10):
            GPIO.output(pins[j],GPIO.LOW)
            
        for j in range(5):
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.LOW)
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
        for j in led_position_tuple_1:
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.HIGH)

        wait(.1)

        for j in led_position_tuple_1:
            GPIO.output(pins[j],GPIO.LOW)

        for j in led_position_tuple_1:
            GPIO.output(pins[j+1],GPIO.HIGH)
        wait(.1)

        for j in led_position_tuple_1:
            GPIO.output(pins[j+1],GPIO.LOW)
            
    display.lcd_clear()
    
def red_leds_follow_right():
    
    display.lcd_display_string(
    'RED LEDS FOLLOW',1)
    display.lcd_display_string(
    'RIGHT:',2)
    
    for i in range(7):

        for j in led_position_tuple_1:
            GPIO.output(pins[j+1],GPIO.HIGH)
            GPIO.output(36,GPIO.HIGH)

        wait(.1)

        for j in led_position_tuple_1:
            GPIO.output(pins[j+1],GPIO.LOW)
            
        for j in led_position_tuple_1:
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)

        for j in led_position_tuple_1:
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
    a10=GPIO.PWM(36,hz)

    dimmer=(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
    
    display.lcd_display_string(
    'RED LEDS BREATHE',1)
    display.lcd_display_string(
    'IN AND OUT:',2)

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
    
def red_leds_sway_inward():
    
    display.lcd_display_string(
    'RED LEDS SWAY',1)
    display.lcd_display_string(
    'INWARD:',2)
    
    for i in range(6):
        for j in led_position_tuple_2:
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.HIGH)
        wait(.1)

        for i in pins:
            GPIO.output(i,GPIO.LOW)

        for j in led_position_tuple_3:
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)
        
        for i in pins:
            GPIO.output(i,GPIO.LOW)
        
    display.lcd_clear()

def red_leds_sway_outward():
    
    display.lcd_display_string(
    'RED LEDS SWAY',1)
    display.lcd_display_string(
    'OUTWARD:',2)
    
    for i in range(6):
        for j in led_position_tuple_3:
            GPIO.output(pins[j],GPIO.HIGH)
            GPIO.output(36,GPIO.HIGH)
        wait(.1)

        for i in pins:
            GPIO.output(i,GPIO.LOW)

        for j in led_position_tuple_2:
            GPIO.output(pins[j],GPIO.HIGH)
        wait(.1)
        
        for i in pins:
            GPIO.output(i,GPIO.LOW)
        
    display.lcd_clear()
    
def red_leds_random():
    
    display.lcd_display_string(
    'RED LEDS RANDOM',1)
    display.lcd_display_string(
    'IN TANDEM:',2)
    
    for i in range(15):
        rand_led=random.randint(0,9)
        GPIO.output(36,GPIO.HIGH)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)    
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)    
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        rand_led=random.randint(0,9)
        GPIO.output(pins[rand_led],GPIO.HIGH)
        wait(.1)

        for j in pins:
            GPIO.output(j,GPIO.LOW)
            
    display.lcd_clear()

# create a functions_tuple

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
    red_leds_follow_right,
    red_leds_sway_inward,
    red_leds_sway_outward,
    red_leds_random,
    red_leds_random)
 
while True:
    try:
        if GPIO.input(16)==0:
            GPIO.output(38,GPIO.LOW)
            display.lcd_clear()
            for i in functions_tuple:
                i();red_led_flash() # call all funcs
                
            display.lcd_display_string(
            'PRESS THE BUTTON',1)
            display.lcd_display_string(
            'AGAIN PLEASE!',2)

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
