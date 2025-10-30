import pgzrun
import pygame
import random

HEIGHT = 700
WIDTH = 700

dots = []

j = pygame.mixer.Sound("Uno\jump1.wav")
h = pygame.mixer.Sound("Uno\sumthing.wav")

def spawn():
    edot = Actor("lil_bad_guy")

global edot
dot = Actor("lil_guy")
dot.pos = 350 , 350
spawn()
edot.pos = random.choice((random.randint(0,200),random.randint(500,700)))

dots.append(dot)
dots.append(edot)

def draw():
    screen.blit("void")
    for i in range(len(dots)):
        dots[i].draw()

def update():
    edot.x += 1
    if keyboard.a:
        dot.x -= 3
    if keyboard.d:
        dot.x += 3
    for i in range(len(dots)):
        j = i + 1
        if j < len(dots):
            if keyboard.k and dots[j].x < dot.x + 20:
                dots.remove(dots[j])
                spawn()
    pass



pgzrun.go()