import pgzrun

WIDTH = 700
HEIGHT = 700

s = Actor("ball")

s.pos = 350 , 650

lvl = 1

j = False

setupp = []

gap = 60

bully = []

def setup():
    for i in range(lvl):
        g = Actor("red_ball")
        g.pos = gap*(i+1) , 20
        setupp.append(g)

setup()

def draw():
    screen.blit("void", (0,0))
    s.draw()
    for i in range(lvl):
        setupp[i].draw()
    for b in bully:
        b.draw()

dx = 3

def update():
    global dx , j
    for i in range(lvl):
        setupp[i].x += dx
        if setupp[i].x > 700 or setupp[i].x < 0:
            dx*=-1
            setupp[i].y += 30
    for b in bully:
        b.y -= 3
        if b.y < 0:
            bully.remove(b)
    if keyboard.a:
        s.x -= 3
    if keyboard.d:
        s.x += 3
    pass

def on_key_down():
    if keyboard.space:
        b = Actor("bullet")
        bully.append(b)
        b.pos = s.x, s.y

pgzrun.go()