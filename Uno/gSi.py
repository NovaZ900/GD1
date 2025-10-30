import pgzrun
import pygame
import random

HEIGHT = 700
WIDTH = 700

score = 0
dots = []

j = pygame.mixer.Sound("Uno\jump1.wav")
h = pygame.mixer.Sound("Uno\sumthing.wav")

dot = Actor("lil_guy")
dot.pos = 350 , 350

def spawn():
    edot = Actor("lil_bad_guy")
    x = random.randint(int(dot.x) - 300,int(dot.x)-150)
    x2 = random.randint(int(dot.x) + 150,int(dot.x) + 300)
    edot.pos = random.choice((x,x2)), 350
    dots.append(edot)

def win_spawn():
    godot = Actor("lil_gold_guy")
    x = random.randint(int(dot.x) - 300,int(dot.x)-150)
    x2 = random.randint(int(dot.x) + 150,int(dot.x) + 300)
    godot.pos = random.choice((x,x2)), 350
    dots.append(godot)


dots.append(dot)
spawn()

def draw():
    screen.blit("void",(0,0))
    for i in range(len(dots)):
        dots[i].draw()

def update():
    global score
    for i in range(len(dots)):
        j = i + 1
        if j < len(dots):
            if dots[j].x > dot.x:
                dots[j].x -= 1
            else:
                dots[j].x += 1
    if keyboard.a:
        dot.x -= 3
    if keyboard.d:
        dot.x += 3
    for i in range(len(dots)):
        j = i + 1
        if j < len(dots):
            if keyboard.k and dots[j].x < dot.x + 60 and dots[j].x > dot.x - 60:
                dots.remove(dots[j])
                if score == 50:
                    win_spawn()
                    if keyboard.k and dots[j].x < dot.x + 60 and dots[j].x > dot.x - 60:
                        dots.remove(dots[j])
                        print("You Win.")
                        exit()
                else:
                    score += 1
                    spawn()
            if dot.colliderect(dots[j]):
                print("You Died.")
                exit()
    pass



pgzrun.go()