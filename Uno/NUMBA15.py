import pygame
from pygame.locals import *

pygame.init()
bg = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
ih = pygame.image.load("Uno/images/space.png")
aih = pygame.image.load("Uno/images/rocket.png")

bg.blit(ih,(0,0))
bg.blit(aih,(50,50))
aih_y = 50
aih_x = 50

keys = [False,False,False,False]
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0]=True
            elif event.key == K_a:
                keys[1]=True
            elif event.key == K_s:
                keys[2]=True
            elif event.key == K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0]=False
            elif event.key == K_a:
                keys[1]=False
            elif event.key == K_s:
                keys[2]=False
            elif event.key == K_d:
                keys[3]=False
    if keys [0]:
        if aih_y > 0:
            aih_y -= 3
    if keys [1]:
        if aih_x > 0:
            aih_x -= 3
    if keys [2]:
        if aih_y < 315:
            aih_y += 3
    if keys [3]:
        if aih_x < 315:
            aih_x += 3
    bg.blit(ih,(0,0))
    bg.blit(aih,(aih_x,aih_y))
    pygame.display.update()