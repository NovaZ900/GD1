import pgzrun

WIDTH = 700
HEIGHT = 700

p = Actor("pong")
b = Actor("ball")

b.pos = 350, 350
p.pos = 350, 700

dx = 3
dy = 3

score = 0

def draw():
    screen.blit("void",(0,0))
    p.draw()
    b.draw()
    screen.draw.text(f"Score: {score}",center = (100,100),fontsize = (20),color = ("white"))
def update():
    global dx
    global dy
    global score
    b.y -= dy
    b.x += dx
    if keyboard.a:
        p.x -= 3
    if keyboard.d:
        p.x += 3
    if p.x < 0:
        p.x += 3
    if p.x > 700:
        p.x -= 3
    if p.colliderect(b):
        score += 1
        dy *= -1
    if b.y > 700:
        exit()
    if b.y < 0:
        dy *= -1
    if b.x > 700:
        dx *= -1
    if b.x < 0:
        dx *= -1

pgzrun.go()