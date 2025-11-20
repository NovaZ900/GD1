import pgzrun
import pygame

WIDTH = 700
HEIGHT = 700

j = False

def on_mouse_down(pos):
    global j, k
    k = pos
    j = True

def draw():
    global k
    screen.fill("white")
    if j == True:
        screen.draw.filled_circle((k), 6, "black")

def update():
    pass



pgzrun.go()