import pgzrun
import pygame
import time

WIDTH = 700
HEIGHT = 700

j = pygame.mixer.Sound("Uno\lazerShoot.wav")
a = pygame.mixer.Sound("Uno\lkok.mp3")
h = ""
k = False
g = []
p = 0
z = -1
l = Actor("op2")
m = Actor("op")
n = Actor("op3")
o = Actor("op4")
g.append(l)
g.append(m)
g.append(n)
g.append(o)

def mmm():
    global h
    h = " "
    j.play()
    time.sleep(1)
    j.stop()
    exit()

def draw():
    screen.fill("black")
    if k == True:
        g[z].draw()
    if k == False:
        screen.draw.text(h, center = (350,350), fontsize = 60, color = "red")

def update():
    global k, h, z
    if p == 0:
        h = "Leave."
        k = False
    if p == 2:
        h = "Please leave."
        k = False
    if p == 4:
        h = "I'M BEGGING YOU, LEAVE."
        k = False
    if p == 6:
        h = "...It's too late."
        k = False
    if p == 1:
        k = True
    if p == 3:
        k = True
    if p == 5:
        k = True
    if p == 7:
        k = True
        mmm()
    pass

def on_mouse_down():
    global p, z
    a.play()
    p += 1
    if p == 1 or p == 3 or p == 5:
        z += 1

pgzrun.go()