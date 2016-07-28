enemy = [ 100, 200, 300, 400] # gird
enemy2 = [100]

def setup():
    size(500, 500)
def draw():
    delay(10)
    y = 450
    background(0)
    for i in enemy:#[the range of the coordinates of enemy[]
        enemyx = i
        for j in range(len(enemy2)):
            enemyY = enemy2[j] # renames the vallue of enemy to [j]
            # add so blocks go down
            fill(255)
            rect(enemyx, enemyY, 20, 20)
            enemy2[j] += .2
    if enemy2[0] >= 450:
        textSize(26)
        fill(255,0,0)
        text("gameover", 100, 200)
    elif enemy2[0] >= 450:
        textSize(26)
        fill(255,0,0)
        text("gameover", 100, 200)
    elif enemy2[0] >= 450:
        textSize(26)
        fill(255,0,0)
        text("gameover", 100, 200)
    elif enemy2[0] >= 450:
        textSize(26)
        fill(255,0,0)
        text("gameover", 100, 200)
        #add break here so it stopps
    elif len(enemy) == 0:
        print(enemy2)
        fill(255)
        textSize(26)
        text("You Win!", 200, 200)

    x = 20
    y = 0
    rect(mouseX-50,450,100,10) #makes the mouse move
    if x > mouseX-50 and x < mouseX+50 and y > 400:
            y = y-2     

shooting = True  
x = 0 # x coordinate of bullet
y = 430 # y coordinate of bullet
def keyPressed():
    global x
    global y
    global shooting
    if shooting == True:
        fill(255)
        rect(mouseX, y+20, 10, 20)
        y = y -10
        if y < 0:
            y = 430
        fill(255)
        rect(mouseX, y, 10, 20)
        if mouseX < enemy[0]+20 and mouseX > enemy[0]-30: # this part deletes each box as shot
            del enemy[0]
        elif mouseX < 220 and mouseX > 170:
            del enemy[1]
        elif mouseX < 320 and mouseX > 270:
            del enemy[2]
        elif mouseX < 420 and mouseX > 370:
            del enemy[3]