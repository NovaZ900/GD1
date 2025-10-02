import pgzrun
import pygame
import random



WIDTH = 700
HEIGHT = 700

jaja = ["ball","drop","satlite","square"]
lvl = 1
sjaja = []
l = Actor("leaf")
an = []

def setup():
    for i in range(lvl):
        s = Actor(random.choice(jaja))
        sjaja.append(s)
    sjaja.append(l)
    random.shuffle(sjaja)
    g = WIDTH / (lvl + 2)
    for i in range(lvl + 1):
        sjaja[i].pos = g * (i + 1) , 20

def anit():
    for i in sjaja:
        a = animate(i , duration = 5, y = 750)
        an.append(a)

setup()
anit()

def draw():
    screen.blit("void", (0,0))
    for i in sjaja:
        i.draw()

def on_mouse_down(pos):
    global lvl, an, sjaja
    for i in sjaja:
        if i.collidepoint(pos):
            if i == l:
                lvl += 1
                for j in an:
                    j.stop()
                an = []
                sjaja = []
                setup()
                anit()
                break
                

pgzrun.go()