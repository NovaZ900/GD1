import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()
HEIGHT = 800
WIDTH = 1000
bg = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GALACTIC SHOWDOWN")
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("images","PlayerShip.png")),(WIDTH, HEIGHT))

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

ORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
SPACEWIDTH = 55
SPACEHEIGHT = 40

running = True
while running:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
            break
