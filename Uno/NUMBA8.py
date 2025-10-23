import pgzrun
import random
import time

WIDTH = 700
HEIGHT = 700

selwidf = WIDTH/3
selheit = HEIGHT/3
bord = []
n_selct = []
t = False
for i in range(3):
    row = [" "]*3
    bord.append(row)
for i in range(3):
    for j in range(3):
        n_selct.append((i,j))
def cross():
    global t
    time.sleep(0.7)
    if n_selct:
        r,c = random.choice(n_selct)
        bord[r][c] = "O"
        n_selct.remove((r,c))
    else:
        t = True
def chek():
    if keyboard.q:
        if bord[0][0] != " ":
            return
        bord[0][0] = "X"
        n_selct.remove((0,0))
        cross()
    if keyboard.w:
        if bord[0][1] != " ":
            return
        bord[0][1] = "X"
        n_selct.remove((0,1))
        cross()
    if keyboard.e:
        if bord[0][2] != " ":
            return
        bord[0][2] = "X"
        n_selct.remove((0,2))
        cross()
    if keyboard.r:
        if bord[1][0] != " ":
            return
        bord[1][0] = "X"
        n_selct.remove((1,0))
        cross()
    if keyboard.t:
        if bord[1][1] != " ":
            return
        bord[1][1] = "X"
        n_selct.remove((1,1))
        cross()
    if keyboard.y:
        if bord[1][2] != " ":
            return
        bord[1][2] = "X"
        n_selct.remove((1,2))
        cross()
    if keyboard.u:
        if bord[2][0] != " ":
            return
        bord[2][0] = "X"
        n_selct.remove((2,0))
        cross()
    if keyboard.i:
        if bord[2][1] != " ":
            return
        bord[2][1] = "X"
        n_selct.remove((2,1))
        cross()
    if keyboard.o:
        if bord[2][2] != " ":
            return
        bord[2][2] = "X"
        n_selct.remove((2,2))
        cross()
def draw():
    screen.fill("white")
    if t:
        screen.draw.text("TIH",center = (350,350),color = "red", fontsize = 200)
    else:
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