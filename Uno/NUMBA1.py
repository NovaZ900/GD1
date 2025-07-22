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
        screen.draw.text("Good shot!",center = (pos),fontsize = (200),color = ("purple"))
        score += 1
    else:
        screen.draw.text("Miss",center = (pos),fontsize = (200),color = ("black"))
        score -= 1


pgzrun.go()