from machine import Pin
import time

sm=PWM(Pin(4),freq=50)
list=[35,70,120]

while True:
    sm.duty(list[0])
    time.sleep(1)
    sm.duty(list[1])
    time.sleep(1)
    sm.duty(list[2])
    time.sleep(1)
