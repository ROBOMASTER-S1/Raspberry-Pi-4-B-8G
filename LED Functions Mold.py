def red_led_flash():

    for i in range(4):
        for j in red_leds:
            GPIO.output(j,1)
            
        for j in yellow_leds:
            GPIO.output(j,0)            
        GPIO.output(RGB_led[0],0)
        wait(led_speed)

        for j in red_leds:
            GPIO.output(j,0)
            
        for j in yellow_leds:
            GPIO.output(j,1)
        GPIO.output(RGB_mix[1],0)
        wait(led_speed)
        
        for j in yellow_leds:
            GPIO.output(j,0)
        GPIO.output(RGB_mix[1],1)
        
def red_led_single_right():
    
        for i in yellow_leds:
            GPIO.output(i,1)
        GPIO.output(RGB_led[0],0)
    
        for i in range(9,-1,-1):
            GPIO.output(red_leds[i],1)        
            wait(led_speed)
            GPIO.output(red_leds[i],0)
            
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
def red_led_single_left():
    
        for i in yellow_leds:
            GPIO.output(i,1)
        GPIO.output(RGB_led[0],0)
    
        for i in range(10):
            GPIO.output(red_leds[i],1)        
            wait(led_speed)
            GPIO.output(red_leds[i],0)
            
        for i in yellow_leds:
            GPIO.output(i,0)
        GPIO.output(RGB_led[0],1)
        
def red_leds_side_to_side_right():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(9,-1,-1):
        GPIO.output(red_leds[i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)

    for i in range(9,-1,-1):
        GPIO.output(red_leds[i],0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)

def red_leds_side_to_side_left():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(10):
        GPIO.output(red_leds[i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)

    for i in red_leds:
        GPIO.output(i,0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_inward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(5):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)
        
    for i in range(5):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_outward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],0)
        
    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_collision_inward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(5):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[0],1)
    
def red_leds_collision_outward():
    
    for i in yellow_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_led[0],0)

    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        wait(led_speed)
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        
    for i in yellow_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[0],1)
    
def red_leds_follow():
    
    for i in range(7):
        for j in range(0,10,2):
            GPIO.output(red_leds[j],1)
            
        GPIO.output(RGB_led[0],0)            
        GPIO.output(yellow_leds[1],1)
        wait(led_speed)
        
        for i in red_leds:
            GPIO.output(i,0)
            
        GPIO.output(RGB_mix[1],0)   
        GPIO.output(yellow_leds[1],0)
        
        for j in range(9,-1,-2):
            GPIO.output(red_leds[j],1)
         
        GPIO.output(RGB_mix[1],0)
        GPIO.output(yellow_leds[0],1)
        wait(led_speed)
        
        for j in red_leds:
            GPIO.output(j,0)
            
        GPIO.output(RGB_mix[1],1)   
        GPIO.output(yellow_leds[0],0)

def red_leds_collision_inward_inverse():
    
    for i in red_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_mix[1],0)

    for i in range(5):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],1)
    
def red_leds_collision_outward_inverse():
    
    for i in red_leds:
        GPIO.output(i,1)
        
    GPIO.output(RGB_mix[1],0)

    for i in range(4,-1,-1):
        GPIO.output(red_leds[0+i],0)
        GPIO.output(red_leds[9-i],0)
        wait(led_speed)
        GPIO.output(red_leds[0+i],1)
        GPIO.output(red_leds[9-i],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
    GPIO.output(RGB_mix[1],1)

def red_leds_stack_right():
    
    for i in range(10):
        for j in range(9,i-1,-1):
            GPIO.output(red_leds[j],1)        
            wait(led_speed)
            GPIO.output(red_leds[j],0)
            
        GPIO.output(red_leds[j],1)
        
    for i in red_leds:
        GPIO.output(i,0)

def red_leds_stack_left():
    
    for i in range(10):
        for j in range(10-i):
            GPIO.output(red_leds[j],1)        
            wait(led_speed)
            GPIO.output(red_leds[j],0)
            
        GPIO.output(red_leds[j],1)
        
    for i in red_leds:
        GPIO.output(i,0)
        
def red_leds_stack_inward():
    
    for i in range(5):
        for j in range(5-i):
            GPIO.output(red_leds[0+j],1)
            GPIO.output(red_leds[9-j],1)
            wait(led_speed)
            GPIO.output(red_leds[0+j],0)
            GPIO.output(red_leds[9-j],0)
            
        GPIO.output(red_leds[j],1)
        GPIO.output(red_leds[9-j],1)
        
    for i in red_leds:
        GPIO.output(i,0) 
        
def red_leds_stack_outward():
    
    for i in range(5):
        for j in range(4,i-1,-1):
            GPIO.output(red_leds[0+j],1)
            GPIO.output(red_leds[9-j],1)
            wait(led_speed)
            GPIO.output(red_leds[0+j],0)
            GPIO.output(red_leds[9-j],0)
            
        GPIO.output(red_leds[j],1)
        GPIO.output(red_leds[9-j],1)
        
    for i in red_leds:
        GPIO.output(i,0)