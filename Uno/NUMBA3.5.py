import pgzrun
import random

WIDTH = 700
HEIGHT = 700

score = 0

s = Actor("satlite")
s.pos = random.randint(0,650),random.randint(0,650)

cord = 0,0

def draw():
    screen.blit("space",(0,0))
    s.draw()
    screen.draw.text(f"{score}/8",center = (100,100),fontsize = (20),color = ("white"))

def update():
    pass

def on_mouse_down(pos):
    global score
    global cord
    cord = pos
    if s.collidepoint(pos):
        if score < 8:
            score += 1



pgzrun.go()