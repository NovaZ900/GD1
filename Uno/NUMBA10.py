import pgzrun
import random

WIDTH = 700
HEIGHT = 700

sercll = []
u = False

def on_mouse_move(pos):
    if u == True:
        sercll.append(pos)

a = 6
r = 0
g = 0
b = 0

def draw():
    global r, g, b
    screen.fill("white")
    for pos in sercll:
        screen.draw.filled_circle((pos), a, (r,g,b))


def update():
    global a, r, g, b, sercll, u
    if keyboard.i:
        a -= 1
    if keyboard.p:
        a += 1
    if keyboard.c:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
    if keyboard.x:
        r = 0
        g = 0
        b = 0
    if keyboard.l:
        sercll = []
    if keyboard.k:
        if u == True:
            u = False
    if keyboard.j:
        if u == False:
            u = True
    if keyboard.o:
        a = 6
    pass

pgzrun.go()