import pgzrun
import pygame

m = pygame.mixer.Sound("Uno\eep.wav")

WIDTH = 700
HEIGHT = 700

s = Actor("ball")

s.pos = 350 , 650

lvl = 1

j = False

setupp = []

gap = 60

bully = []

score = 0

def setup():
    for i in range(lvl):
        g = Actor("red_ball")
        g.pos = gap*(i+1) , 20
        setupp.append(g)

setup()

def draw():
    screen.blit("void", (0,0))
    s.draw()
    for r in setupp:
        r.draw()
    for b in bully:
        b.draw()

dx = 3
dy = 20

def update():
    global dx , j , lvl, dy, setupp, bully
    jb = 0
    leng = lvl - jb
    for r in setupp:
        r.x += dx
        r.y = dy
    if setupp[-1].x > 700 or setupp[0].x < 0:
        dx*=-1
        dy += 30
    for b in bully:
        b.y -= 3
        if b.y < 0: 
            bully.remove(b)
    if keyboard.a:
        s.x -= 3
    if keyboard.d:
        s.x += 3
    for b in bully:
        for r in setupp:
            if b.colliderect(r):
                bully.remove(b)
                setupp.remove(r)  
                break
    if not setupp:
        lvl += 1
        setup()  
    for r in setupp:
        if r.colliderect(s):
            exit()
    if lvl > 10:
        setupp = []
        bully = []
    pass

def on_key_down():
    if keyboard.space:
        m.play()
        b = Actor("bullet")
        bully.append(b)
        b.pos = s.x, s.y

pgzrun.go()