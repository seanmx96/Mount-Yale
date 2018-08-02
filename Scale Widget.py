from tkinter import *

def update (duty):
    pwm.ChangeDutyCycle(float(duty))
    
master = Tk()
w = Scale(master, from_=0, to=100, orient=HORIZONTAL, command = update)
w.pack()

