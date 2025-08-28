import pgzrun
import random

WIDTH = 700
HEIGHT = 700

score = 0
cord = 0,0

a = []

c = Actor("comet")
c.pos = -20 ,random.randint(20,680)

def draw():
    screen.blit("space",(0,0))
    c.draw()
    screen.draw.text(f"Score:{score}",center = (40,30),fontsize = (20),color = ("white"))

def update():
    c.x += 5
    if c.x > 850:
        c.pos = -20 ,random.randint(20,680)

def on_mouse_down(pos):
    global score
    global cord
    cord = pos
    if c.collidepoint(pos):
        score += 1
        c.pos = -20 ,random.randint(20,680)


pgzrun.go()