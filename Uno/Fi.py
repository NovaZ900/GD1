import pgzrun
import random
WIDTH = 700
HEIGHT = 700

def draw():
    b.draw()
    f.draw()
def update():
    f.y += 3
    if keyboard.left:
        b.x -= 3
    if keyboard.right:
        b.x += 3
    if b.colliderect(f):
        f.pos = random.randint(0,650), -10
    if f.y > 700:
        f.pos = random.randint(0,650), -10

b = Actor("bee")
f = Actor("flower (1)")

f.pos = random.randint(0,650), -10

pgzrun.go()