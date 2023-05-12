# 16b Binary Translator Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electroics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1 or more depending
# 74HC595 shift register = 3
# LEDs = 24
# 220 ohm resistor = 24
# jumper wire = 38 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 16b Binary Translator Python program example:

# This Raspberry Pi 4 Python program allows
# users to input decimal numbers, then
# translate them into binary, hexadecimal
# and decimal values using three 74HC595
# shift registers.

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

# import functions:

import RPi.GPIO as GPIO
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

port_pin=11,13

GPIO.setup(port_pin[0],GPIO.OUT)
GPIO.setup(port_pin[1],GPIO.OUT)

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

latch=35
data_bit=37
clock=33
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
byte_range=16_777_216 # from 0 to 16,777,216

control_shift=data_bit,latch,clock

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

message='\n24B TRANSLATOR','ENTER 24B NUMBER: '
value_error='\nBYTE VALUES ONLY','PLEASE: 0-16777215'
index_error='\nVALUE EXCEEDS','16B RANGE 0-16777215'

sentence='\nComputer Binary Num:','= \
Human Decimal Num: '

beep_on='''
GPIO.output(port_pin[0],1)
GPIO.output(port_pin[1],1)
'''
beep_off='''
GPIO.output(port_pin[0],0)
GPIO.output(port_pin[1],0)
'''

for i in control_shift:GPIO.setup(i,GPIO.OUT)

# Create two functions called
# clear_all_data_bits and shift_all_data_bits.


def clear_all_data_bits():
    
    for i in range(24):
        GPIO.output(latch,0)
        GPIO.output(data_bit,0) # set all 16 data bits to 0/off
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
        
clear_all_data_bits() # call the function
        
def shift_all_data_bits():
    
    clear_all_data_bits() # call the function
    
    for i in range(byte):            
        bin=f'{byte:b}'
        for j in range(24):                
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
while True:
    try:
        while True:
            print(message[0])
            try:
                byte=int(input(message[1]).strip())                
                if byte>=byte_range:                    
                    for i in range(2):
                        print(index_error[i])
                    wait(2)
                    break
                print(f'{sentence[0]} {byte:b} \
{sentence[1]}{byte:,d}')
                
                shift_all_data_bits() # call the function

            except ValueError:
                for i in range(2):
                    print(value_error[i])        
                wait(2)
                break
            
            except IndexError:
                pass
            for x in range(byte):
                print(f'{x+1:b}',end=' = ')
                print(x+1)
                exec(beep_on)
                wait(.004)
                exec(beep_off)
                wait(.004)
                wait(.5)
            wait(2)
            
            clear_all_data_bits() # call the function
            
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

    except KeyboardInterrupt:
        exec(stop_program_message)
        
        clear_all_data_bits() # call the function
            
        GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
        break