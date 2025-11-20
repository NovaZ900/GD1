import pgzrun

WIDTH = 700
HEIGHT = 700

g = 12
j = 350
k = 350

gjh = (350-g, 350-g)
ghj = (350+g, 350+g)

cord = 0,0

def draw():
    screen.fill("white")
    screen.draw.filled_circle((350,350), g, "blue")

def update():
    pass

def on_mouse_down(pos):
    global g
    global cord
    cord = pos
    if cord > gjh and cord < ghj:
        g += 5


pgzrun.go()