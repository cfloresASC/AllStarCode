from random import * 
size(700, 700)   
background(04, 250, 0)
fill(0)
rect(0, 70, 700, 100)
fill(255)
rect(0, 110, 100, 20)
rect(200, 110, 100, 20)
rect(400, 110, 100, 20)
rect(600, 110, 100, 20)
blue = color(0,0,255)
red = color(255, 0, 0)
green = color(0,255,0)
black = color(0,0,0)
white = color(255, 255, 255)
random = randint(0, 256)
def make_car(x, y, name, colora, colorb):
    if colora == blue:
        fill(0,0,255)
    elif colora == red:
        fill(255,0,0)
    elif colora == green:
        fill(0,255,0)        
    elif colora == black:
        fill(0,0,0)
    elif colora == white:
        fill(255,255,255)
    else:
        fill(random)  
    noStroke()      
    rect(x, y, 200, 50)
    triangle(390,100,390,150,440,125)
    rect(x, y, 200, 50)
    if colorb == blue:
        fill(0,0,255)
    elif colorb == red:
        fill(255,0,0)
    elif colorb == green:
        fill(0,255,0)        
    elif colorb == black:
        fill(0,0,0)
    elif colorb == white:
        fill(255,255,255)
    else:
        fill(random)    
    ellipse(x, y-10, 30, 15)      
    ellipse(x, y+60, 30, 15)      
    ellipse(x+200, y-10, 30, 15)      
    ellipse(x+200, y+60, 25, 15)
    textSize(25)
    text(name, x + 90, y + 20)
make_car(190, 100, "car", blue, red)