import pygame

pygame.init()
bg = pygame.display.set_mode((700,700))

a = pygame.image.load("Uno/images/juja.png")
b = pygame.image.load("Uno/images/jujaj.png")
c = pygame.image.load("Uno/images/jujaju.png")
d = pygame.image.load("Uno/images/jujajuj.jpg")
bgo = pygame.image.load("Uno/images/void.png")
bg.blit(bgo,(0,0))
bg.blit(a,(50,50))
bg.blit(b,(50,150))
bg.blit(c,(50,250))
bg.blit(d,(50,350))
font = pygame.font.SysFont("Times New Roman", 40)
text = font.render("Subway Surfers", True, "white")
text2 = font.render("Temple Run", True, "white")
text3 = font.render("Candy Crush", True, "white")
text4 = font.render("Ludo", True, "white")
bg.blit(text,(400,50))
bg.blit(text2,(400,150))
bg.blit(text3,(400,250))
bg.blit(text4,(400,350))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            ih = pygame.mouse.get_pos()
            pygame.draw.circle(bg, "white", ih, 15, 0)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            aih = pygame.mouse.get_pos()
            pygame.draw.line(bg, "white", ih, aih, 5)
            pygame.draw.circle(bg, "white", aih, 15, 0)
            pygame.display.update()
    pygame.display.update()