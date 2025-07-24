import pgzrun
import random
WIDTH = 700
HEIGHT = 700

def draw():
    screen.blit("aja",(0,0))
    b.draw()
    f.draw()
def update():
    if keyboard.left:
        b.x -= 3
    if keyboard.right:
        b.x += 3
    if keyboard.up:
        b.y -= 3
    if keyboard.down:
        b.y += 3
    if b.colliderect(f):
        f.pos = random.randint(0,650), random.randint(0,650)

b = Actor("bee")
f = Actor("flower (1)")

f.pos = random.randint(0,650), random.randint(0,650)

pgzrun.go()