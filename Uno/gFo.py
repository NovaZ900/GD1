import pgzrun

WIDTH = 700
HEIGHT = 700

s = Actor("ball")
b = Actor("bullet")

s.pos = 350 , 680

lvl = 1
sl = []
anjj = []

k = False

b.pos = s.pos

def setup():
    for i in range(lvl):
        sll = Actor("red_ball")
        sl.append(sll)
    g = WIDTH / (lvl + 2)
    for i in range(lvl):
        sl[i].pos = g * (i + 1) , 20

setup()

def draw():
    screen.blit("void", (0,0))
    for i in sl:
        i.draw()
    if k == True:
        b.draw()
    s.draw()

def update():
    global k
    global lvl
    b.y -= 3
    if keyboard.a:
        s.x -= 3
    if keyboard.d:
        s.x += 3
    if keyboard.space:
        k = True
    for i in range(lvl):
        if b.colliderect(sl[i]):
            lvl += 1
        if s.colliderect(sl[i]):
            exit()
            
    

pgzrun.go()