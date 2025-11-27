import pgzrun
import pygame
import time

WIDTH = 700
HEIGHT = 700

j = pygame.mixer.Sound("Uno\chezburger.mp3")
a = pygame.mixer.Sound("Uno\lkok.mp3")
h = ""
k = False
g = []
p = 0
l = Actor("op2")
m = Actor("op")
n = Actor("op3")
o = Actor("op4")
g.append(l)
g.append(m)
g.append(n)
g.append(o)

def mmm():
    j.play()
    time.sleep(1)
    j.stop()
    exit()

def draw():
    screen.fill("black")
    while k == True:
        g[p-1].draw()
    while k == False:
        screen.draw.text(h, center = (350,350), fontsize = 100, color = "red")

def update():
    global h, k
    while p == 0:
        h = "Leave."
        k = False
    while p == 2:
        h = "Please leave."
        k = False
    while p == 4:
        h = "I'M BEGGING YOU, LEAVE."
        k = False
    while p == 6:
        h = "...It's too late."
        k = False
    if p == 7:
        k = True
        mmm()
    pass

def on_mouse_down():
    global p
    a.play()
    p += 1


pgzrun.go()