import RPi.GPIO as GPIO # GPIO library needed to access GPIO pins
import time # time library needed to pause output

GPIO.setmode(GPIO.BOARD) # initialize GPIO mode to board
GPIO.setup(40, GPIO.OUT) # send signal out on pin 40
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # receives button signal on pin 37

try:
    while True: # Alternates LED on/off for 1 second each way
        input_value = GPIO.input(37)
        if input_value == False:
            GPIO.output(40, True)
            time.sleep(1)
            GPIO.output(40, False)
            time.sleep(1)
        else:
            GPIO.output(40, True)
    
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly
    print("Keyboard Interrupt")
    
except:
    print ("Other error or exception occurred!")
    
finally:
    print ("clean up")
    GPIO.cleanup() # this ensures a clean exit