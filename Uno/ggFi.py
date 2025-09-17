import pgzrun
import pygame
import time

WIDTH = 700
HEIGHT = 700

h = pygame.mixer.Sound("Uno\_blip.wav")
g = pygame.mixer.Sound("Uno\hitHurt.wav")
s = pygame.mixer.Sound("Uno\_tone.wav")
v = pygame.mixer.Sound("Uno\_victory1.wav")

l = []

p = Actor("pong2")
p.pos = 13 , 350
p2 = Actor("pong2")
p2.pos = 687 , 350
b = Actor("ball")
b.pos = 350 , 350
l.append(p)
l.append(p2)
l.append(b)

dx = 3
dy = 3

score = 0
score2 = 0

def draw():
    global l
    screen.blit("void",(0,0))
    for gh in l:
        gh.draw()
    screen.draw.text(f"P1 Score: {score2}",center = (50,50),fontsize = (20),color = ("white"))
    screen.draw.text(f"P2 Score: {score}",center = (650,50),fontsize = (20),color = ("white"))
    if score == 100:
        l = []
        v.play()
        screen.draw.text(f"Player 2 Wins!",center = (350,350),fontsize = (200),color = ("white"))
        time.sleep(5)
        exit()
    if score2 == 100:
        l = []
        v.play()
        screen.draw.text(f"Player 1 Wins!",center = (350,350),fontsize = (200),color = ("white"))
        time.sleep(5)
        exit()
    
def update():
    global dx, dy, score, score2
    b.y -= dy
    b.x += dx
    if keyboard.w:
        p.y -= 3
    if keyboard.s:
        p.y += 3
    if keyboard.up:
        p2.y -= 3
    if keyboard.down:
        p2.y += 3
    if p.y < 0:
        p.y += 3
    if p.y > 700:
        p.y -= 3
    if p2.y < 0:
        p2.y += 3
    if p2.y > 700:
        p2.y -= 3
    if p.colliderect(b) or p2.colliderect(b):
        h.play()
        dx *= -1
    if b.x > 700:
        score2 += 1
    if b.x < 0:
        score += 1
    if b.y < 0:
        g.play()
        dy *= -1
    if b.y > 700:
        g.play()
        dy *= -1
    if b.x < 0:
        score += 1
        b.pos = 350, 350
    if b.x > 700:
        score2 += 1
        b.pos = 350, 350

pgzrun.go()