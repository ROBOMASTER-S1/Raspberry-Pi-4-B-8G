# 24b Shift Register Fun Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1 or more depending
# 74HC595 shift register = 2
# LEDs = 24
# 220 ohm resistor = 24
# jumper wire = 36 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 24b Shift Register Fun Python program example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how three 8b 74HC595 shift registers work.

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
# program example.

# import functions:

import RPi.GPIO as GPIO,random
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

# Create variables for the latch, data bit and the clock.

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: Python executes its programs from the top, downward.
# You must place these variables in this correct order as shown.
# These pinout values won't execute right if you don't.

latch=19
data_bit=21
clock=15
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
led_speed=1,.1 # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

led_intro=[
    '101000000000000000000101',
    '000111100000000001111000',
    '011000011111111110000011']

led_show=[
    '100100000000000000001100','110010000000000000010110','100001000000000000100100','110000100000000001000110',
    '001000010000000010000001','010000011000000110000010','001000011100001110000001','010000011110011110000010',
    '001000011111111110000001','010000001111111100000010','001000000111111000000001','010000000011110000000010',
    '001000000001100000000001','010000000010010000000010','001000000100001000000001','010000001000000100000010',
    '001000010000000010000001','110000100000000001000110','100001100000000001100100','110011100000000001110110',
    '100111100000000001111100','110111000000000000111110','100110000000000000011100','110100000000000000001110',
    '100110000000000000011100','110111000000000000111110','100111100000000001111100','110011100000000001110110',
    '100001100000000001100100','110000100000000001000110','001000010000000010000001','010000001000000100000010',
    '001000000100001000000001','010000000010010000000010','001000000001100000000001','010000000010010000000010',
    '001000000100001000000001','010000001000000100000010','001000010000000010000001','010000011000000110000010',
    '001000011100001110000001','010000011110011110000010','001000011111111110000001','010000001111111100000010',
    '001000000111111000000001','010000000011110000000010','001000000001100000000001','101111100000000001111101',
    '011000011111111110000011','101111100000000001111101','011000011111111110000011','101111100000000001111101',    
    '001111111110011111111001','010111111100001111111010','001111111000000111111001','010111110000000011111010',
    '001111100000000001111001','110111000000000000111110','100110000000000000011100','110100000000000000001110',
    '111000011111111110000111','000111100000000001111000','111000011111111110000111','000111100000000001111000',
    '111000011111111110000111','001000000000000000000001','000100000000000000001000','000010000000000000010000',
    '000001000000000000100000','000000100000000001000000','000000010000000010000000','000000001000000100000000',
    '000000000100001000000000','000000000010010000000000','000000000001100000000000','001000000001100000000001',
    '000100000001100000001000','000010000001100000010000','000001000001100000100000','000000100001100001000000',
    '000000010001100010000000','000000001001100100000000','000000000101101000000000','000000000011110000000000',
    '001000000011110000000001','000100000011110000001000','000010000011110000010000','000001000011110000100000',
    '000000100011110001000000','000000010011110010000000','000000001011110100000000','000000000111111000000000',
    '001000000111111000000001','000100000111111000001000','000010000111111000010000','000001000111111000100000',
    '000000100111111001000000','000000010111111010000000','000000001111111100000000','001000001111111100000001',
    '000100001111111100001000','000010001111111100010000','000001001111111100100000','000000101111111101000000',
    '000000011111111110000000','001000011111111110000001','000100011111111110001000','000010011111111110010000',
    '000001011111111110100000','000000111111111111000000','001000111111111111000001','000100111111111111001000',
    '000010111111111111010000','000001111111111111100000','001001111111111111100001','000101111111111111101000',
    '000011111111111111110000','001011111111111111110001','000111111111111111111000','001111111111111111111001',
    '001111111110011111111001','001111111100001111111001','001111111000000111111001','001111110000000011111001',
    '001111100000000001111001','001111000000000000111001','001110000000000000011001','001100000000000000001001',
    '001000000000000000000001','000000000001100000000000','000000000010010000000000','000000000100001000000000',
    '000000001000000100000000','000000010000000010000000','000000100000000001000000','000001000000000000100000',
    '000010000000000000010000','000100000000000000001000','001000000000000000000001','001000000001100000000001',
    '001000000010010000000001','001000000100001000000001','001000001000000100000001','001000010000000010000001',
    '001000100000000001000001','001001000000000000100001','001010000000000000010001','001100000000000000001001',
    '001100000001100000001001','001100000010010000001001','001100000100001000001001','001100001000000100001001',
    '001100010000000010001001','001100100000000001001001','001101000000000000101001','001110000000000000011001',
    '001110000001100000011001','001110000010010000011001','001110000100001000011001','001110001000000100011001',
    '001110010000000010011001','001110100000000001011001','001111000000000000111001','001111000001100000111001',
    '001111000010010000111001','001111000100001000111001','001111001000000100111001','001111010000000010111001',
    '001111100000000001111001','001111100001100001111001','001111100010010001111001','001111100100001001111001',
    '001111101000000101111001','001111110000000011111001','001111110001100011111001','001111110010010011111001',
    '001111110100001011111001','001111111000000111111001','001111111001100111111001','001111111010010111111001',
    '001111111100001111111001','001111111001100111111001','001111111010010111111001','001111111100001111111001',
    '001111111101101111111001','001111111110011111111001','001111111111111111111001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','000000000000000000000000','110111111111111111111110','000000000000000000000000',
    '110111111111111111111110','000000000000000000000000','110111111111111111111110','000000000000000000000000',
    '110111111111111111111110','000000000000000000000000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000101010101010101010001','001010101010101010101000',
    '000101010101010101010001','001010101010101010101000','000000000000000000000000','110111111111111111111110',
    '000000000000000000000000','110111111111111111111110','000000000000000000000000','110111111111111111111110',
    '000000000000000000000000','110111111111111111111110','000000000000000000000000']

for i in range(24):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)

try:
    for i in led_intro:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[0])
        
    for i in led_show:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
    
    for i in range(35):
        for j in range(24):
            randvalue=random.randint(0,1)
            GPIO.output(latch,0)
            GPIO.output(data_bit,randvalue)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
    for i in range(2):
        for j in range(24):
            randvalue=random.randint(0,1)
            GPIO.output(latch,0)
            GPIO.output(data_bit,randvalue)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            wait(led_speed[1])
            
    for i in range(24):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,0)
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
        
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

except KeyboardInterrupt:
    exec(stop_program_message) # GPIO notification message
    
    for i in range(24):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,0)
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    GPIO.cleanup()
