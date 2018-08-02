import RPi.GPIO as GPIO
import time # time library needed to pause output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)

# Alternates LED on/off for 1 second each way
while True:
    GPIO.output(38, True)
    time.sleep(1)
    GPIO.output(38, False)
    time.sleep(1)
