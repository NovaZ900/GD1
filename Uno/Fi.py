import pgzrun
import random
WIDTH = 700
HEIGHT = 700

b = Actor("spike")
f = Actor("balloon")
b.y = 700

f.pos = random.randint(0,650), -10

def draw():
    screen.blit("void",(0,0))
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

pgzrun.go()