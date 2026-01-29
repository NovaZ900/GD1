import pygame
import time

pygame.init()
screen = pygame.display.set_mode((700,700))

pygame.display.set_caption("Burthdae!!!")
bg = pygame.image.load("Uno/images/kfig.jpg")
bg = pygame.transform.scale(bg,(700,700))
j = pygame.mixer.Sound("Uno/happy-wheels-victory-made-wihh-Voicemod.mp3")
running = True
j.play()

while running:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    font = pygame.font.SysFont("Times New Roman",72)
    text = font.render("Happy", True, (0,0,0))
    text2 = font.render("Burthdae!!!", True, (0,0,0))
    screen.blit(text,(250,200))
    screen.blit(text2,(200,325))
    pygame.display.update()
    time.sleep(2)
    text3 = font.render("y e h", True, (0,0,0))
    screen.blit(text3, (250,380))
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        ih = pygame.mouse.get_pos()
        pygame.draw.circle(bg, "black", ih, 15, 0)
    elif event.type == pygame.MOUSEBUTTONUP:
        aih = pygame.mouse.get_pos()
        pygame.draw.line(bg, "black", ih, aih, 5)
        pygame.draw.circle(bg, "black", aih, 15, 0)
    
