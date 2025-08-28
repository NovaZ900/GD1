import pgzrun
import random
import time

WIDTH = 700
HEIGHT = 700

score = 0
tim = time.time()
totl = 0

ss = []
sc = []
ec = []
sn = 1
for i in range(8):
    s = Actor("satlite")
    s.pos = random.randint(10,650),random.randint(10,650)
    ss.append(s)

cord = 0,0

def draw():
    screen.blit("space",(0,0))
    for i in range(8):
        ss[i].draw()
        screen.draw.text(f"{i+1}",center = (ss[i].x,ss[i].y-10),color = ("white"))
    
    for i in range(len(sc)):
        screen.draw.line(sc[i],ec[i],color = "white")
    screen.draw.text(f"{score}/7",center = (100,100),fontsize = (20),color = ("white"))
    
    if score == 7:
        screen.blit("void",(0,0))
        screen.draw.text(f"YOU WIN",center = (350,350),fontsize = (150),color = ("white"))
    totl = time.time() - tim
    screen.draw.text(f"{round(totl,2)}",center = (100,50))




def update():
    pass

def on_mouse_down(pos):
    global score
    global cord
    global sn
    global sc
    global ec
    cord = pos
    c = False
    for i in range(8):
        if ss[i].collidepoint(pos):
            c = True
            if i == sn:
                sc.append(ss[i-1].pos)
                ec.append(ss[i].pos)
                if score < 7:
                    score += 1
                sn += 1
            else:
                sc = []
                ec = []
                sn = 1
    if not c:
        sc = []
        ec = []
        sn = 1

def end():
    print("")
clock.schedule(end,2)

pgzrun.go()