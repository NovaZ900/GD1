import pgzrun
import random
import time

WIDTH = 700
HEIGHT = 700

selwidf = WIDTH/3
selheit = HEIGHT/3
bord = []

for i in range(3):
    row = [" "]*3
    bord.append(row)
def cross():
    time.sleep(3)
    g = bord[random.randint(0,2)][random.randint(0,2)]
    g = "O"
def chek():
    if keyboard.q:
        bord[0][0] = "X"
        cross()
    if keyboard.w:
        bord[0][1] = "X"
        cross()
    if keyboard.e:
        bord[0][2] = "X"
        cross()
    if keyboard.r:
        bord[1][0] = "X"
        cross()
    if keyboard.t:
        bord[1][1] = "X"
        cross()
    if keyboard.y:
        bord[1][2] = "X"
        cross()
    if keyboard.u:
        bord[2][0] = "X"
        cross()
    if keyboard.i:
        bord[2][1] = "X"
        cross()
    if keyboard.o:
        bord[2][2] = "X"
        cross()
def draw():
    screen.fill("white")
    screen.draw.line((WIDTH/3,0),(WIDTH/3,HEIGHT),"black")
    screen.draw.line((2*WIDTH/3,0),(2*WIDTH/3,HEIGHT),"black")
    screen.draw.line((0,HEIGHT/3),(WIDTH,HEIGHT/3),"black")
    screen.draw.line((0,2*HEIGHT/3),(WIDTH,2*HEIGHT/3),"black")
    for i in range(3):
        for j in range(3):
            x = ((selwidf * j) + (selwidf/2))
            y = ((selheit * i) + (selheit/2))
            screen.draw.text(bord[i][j], center = (x,y), color = "black", fontsize = 160)

def update():
    chek()
    pass

pgzrun.go()