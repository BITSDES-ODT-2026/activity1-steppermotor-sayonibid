from machine import Pin  #code5
import time

in1= Pin(4,Pin.OUT)
in2= Pin(5,Pin.OUT)
in3= Pin(12,Pin.OUT)
in4= Pin(27,Pin.OUT)

pb1=Pin(21,Pin.IN,Pin.PULL_UP)
pb2=Pin(14,Pin.IN,Pin.PULL_UP)

pos=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

my_t= 0.005 #0.005ms

while True:
    pb1_val=pb1.value()
    pb2_val=pb2.value()
    
    if pb1_val==0:
        for p in range(125):
            for i in pos:
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                time.sleep(my_t)
            
    if pb2_val==0:
        for q in range(125):
            for i in reversed(pos):
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                time.sleep(my_t)
            
        
