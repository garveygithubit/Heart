import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

if __name__ == "__main__":
    speed(0)  # Use the maximum speed, 0 is fastest
    bgcolor("black")
    color("red")
    
    penup()
    goto(0, 0)
    pendown()
    
    for i in range(6000):
        goto(hearta(i / 100) * 20, heartb(i / 100) * 20)
    
    done()
