import pgzrun
import random

WIDTH = 1500
HEIGHT = 800

score = 0

a = Actor("kaka_resized")
a.pos = random.randint(70,1430),random.randint(50,750)

def draw():
    screen.fill("dark blue")
    a.draw()
    screen.draw.text(f"SCORE:{score}",center = (100,100),fontsize = (20),color = ("black"))

def update():
    pass

def on_mouse_down(pos):
    global score
    if a.collidepoint(pos):
        a.pos = random.randint(70,1430),random.randint(50,750)
        score += 1
    else:
        score -= 1

pgzrun.go()