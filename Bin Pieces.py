import RPi.GPIO as GPIO,threading
from time import sleep as wait

# Breadboard Metod:
# Actual GPIO Pinouts

red_bin_leds=[13,15,19,21,23,29,31,33]

blue_leds=[11,35]

yellow_leds=[7,37]

RGB_led=[18,16,12]

RGB_mix=[[18,12],[18,16],[16,12]]

RGB_logic=[18,16,12,[18,16],
[18,12],[12,16],[18,16,12,16]]

hz=500 # LED dimmer herz value

led_speed=.8

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

for i in red_bin_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
for i in yellow_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in blue_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in RGB_led:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)

on_off=0,1

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)    
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
    
for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(6):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
    
for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(7):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
    
for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0) 
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
    
for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(6):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
    
for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

for i in red_bin_leds:
    GPIO.output(i,1)