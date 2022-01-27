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
display=drivers.Lcd()

for i in pins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)

GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
display.lcd_backlight(0)

print('starting program:')
print('\nPress the Magic Button:')

try:
    while True:
        if GPIO.input(16)==0 :
            display.lcd_backlight(1)
            display.lcd_clear()

            display.lcd_display_string(
                'RED LED',1)
            display.lcd_display_string(
                'Back/Forth:',2)

            for i in range(2):
                for j in range(0,9):
                    GPIO.output(pins[j],GPIO.HIGH)
                    wait(.05)
                    GPIO.output(pins[j],GPIO.LOW)

                for j in range(9,0,-1):
                    GPIO.output(pins[j],GPIO.HIGH)
                    wait(.05)
                    GPIO.output(pins[j],GPIO.LOW)
            display.lcd_clear()

            display.lcd_display_string(
                'RED LEDS Flash:',1)

            for i in range(5):
                for j in range(10):
                    GPIO.output(pins[j],GPIO.HIGH)
                wait(.1)

                for j in range(10):
                    GPIO.output(pins[j],GPIO.LOW)
                wait(.1)
            display.lcd_clear()

            for j in range(10):
                GPIO.output(pins[j],GPIO.HIGH)

            display.lcd_display_string(
                'RED LED',1)
            display.lcd_display_string(
                'Back/Forth In:',2)

            for i in range(2):
                for j in range(0,9):
                    GPIO.output(pins[j],GPIO.LOW)
                    wait(.05)
                    GPIO.output(pins[j],GPIO.HIGH)

                for j in range(9,0,-1):
                    GPIO.output(pins[j],GPIO.LOW)
                    wait(.05)
                    GPIO.output(pins[j],GPIO.HIGH)

                for j in range(10):
                    GPIO.output(pins[j],GPIO.HIGH)
            display.lcd_clear()

            display.lcd_display_string(
                'RED LEDS Flash:',1)

            for i in range(6):
                for j in range(10):
                    GPIO.output(pins[j],GPIO.HIGH)
                wait(.1)

                for j in range(10):
                    GPIO.output(pins[j],GPIO.LOW)
                wait(.1)
            display.lcd_clear()

            for i in pins:
                GPIO.output(i,GPIO.LOW)

            display.lcd_display_string(
                'RED LEDS.',1)
            display.lcd_display_string(
                'Side to Side:',2)

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

            display.lcd_display_string(
                'RED LEDS Flash:',1)

            for i in range(5):
                for j in range(10):
                    GPIO.output(pins[j],GPIO.HIGH)
                wait(.1)

                for j in range(10):
                    GPIO.output(pins[j],GPIO.LOW)
                wait(.1)
            display.lcd_clear()

            for i in pins:
                GPIO.output(i,GPIO.LOW)
            display.lcd_backlight(0)

except KeyboardInterrupt:
    print('\nStop program Execution/run:')
    print('cleanup/release all pinouts to LOW state.')
    display.lcd_clear()
    display.lcd_backlight(0)
    GPIO.cleanup()
