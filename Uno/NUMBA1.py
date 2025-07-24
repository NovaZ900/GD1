import pgzrun
import random

WIDTH = 1500
HEIGHT = 800

score = 0

a = Actor("kaka_resized") # type: ignore
a.pos = random.randint(70,1430),random.randint(50,750)

m = ""
cord = 0,0

def draw():
    screen.fill("dark blue") # type: ignore
    a.draw()
    screen.draw.text(f"SCORE:{score}",center = (100,100),fontsize = (20),color = ("black"))
    screen.draw.text(m,center = (cord),fontsize = (100),color = ("purple"))

def update():
    pass

def on_mouse_down(pos):
    global score
    global m
    global cord
    cord = pos
    if a.collidepoint(pos):
        m = "NICE SHOT!"
        a.pos = random.randint(70,1430),random.randint(50,750)
        score += 1
    else:
        m = "u missed bozo"
        if score > 0:
            score -= 1


pgzrun.go()