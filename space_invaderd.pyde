x = 0
y = 0
def setup():
    loadImage("space.png")

    size(614, 335)
def draw():
    global x 
    global y
    rect(mouseX-50,450,100,10)
    if x > mouseX-50 and x < mouseX+50 and y > 400:
        y = y-2