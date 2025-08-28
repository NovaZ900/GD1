import pgzrun
import random

WIDTH = 700
HEIGHT = 700

a = ["ball","leaf","drop"]
jl = []
w = 2
for i in range(3):
    aj = Actor(a[i])
    jl.append(aj)

score = 0

for i in range(w):
    j = i + 1
    if w == 2:
        p = 700 / 3
    else:
        p = 700 / 4
    jl[i].pos = j * p , 20

def draw():
    screen.blit("void",(0,0))
    global n
    global a
    global j
    global jl
    global w
    global p
    screen.draw.text(f"Score:{score}",center = (40,30),fontsize = (20),color = ("white"))
    for i in range(w):
        j = i + 1
        if w == 2:
            p = 700 / 3
        else:
            p = 700 / 4
        jl[i].pos = j * p , 20
        jl[i].draw()

def update():
    for i in range(w):
        jl[i].y += 5
    for i in range(w):
            if jl[i].y > 750:
                for i in range(w):
                    if w == 2:
                        p = 700 / 3
                        jl[i].pos = j * p , 20
                    else:
                        p = 700 / 4
                        jl[i].pos = j * p , 20

def on_mouse_down(pos):
    global cord
    global w
    global score
    global p
    cord = pos
    c = False
    for i in range(w):
        if jl[1].collidepoint(pos):
            c = True
            if c == True:
                if w < 3:
                    score += 1
                    w += 1
                    for i in range(w):
                        p = 700 / 4
                        jl[i].pos = j * p , 20
                if w > 3:
                    exit()
            else:
                if score > 0:
                    score -= 1
                if w > 2:
                    w -= 1
                for i in range(w):
                    p = 700 / 3
                    jl[i].pos = j * p , 20

pgzrun.go()