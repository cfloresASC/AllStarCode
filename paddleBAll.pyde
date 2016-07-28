from random import *
def setup():
    size(500,500)
    background(25,320,120)
x = 250
y = 250
a = False
b = False
c = False
def draw():
    global x
    global y
    global a 
    global b
    background(23,242,123)    
    fill(255, 210, 230)
    ellipse(x,y,45,45)
    if a == False:
        x += 2
        y += 1
        if x > 475:
            a = True
    elif a == True:
        x -= 2
        y -= 2
        if x < 25:
            a = False
    if b == False:
        x += 2
        y += 4
        if y > 475:
            b = True
    elif b == True:
        x += 1
        y -= 2
        if y < 25:
            b = False
    rect(mouseX-50,450,100,10)
    if x > mouseX-50 and x < mouseX+50 and y > 400:
        y = y-2