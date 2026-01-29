import pygame

pygame.init()
bg = pygame.display.set_mode((700,700))

a = pygame.image.load("Uno/images/juja.png")
b = pygame.image.load("Uno/images/jujaj.png")
c = pygame.image.load("Uno/images/jujaju.png")
d = pygame.image.load("Uno/images/jujajuj.jpg")

running = True

while running:
    bg.fill("white")
    bg.blit(a,(50,50))
    bg.blit(b,(50,150))
    bg.blit(c,(50,250))
    bg.blit(d,(50,350))
    font = pygame.font.SysFont("Times New Roman", 40)
    text = font.render("Subway Surfers", True, (0,0,0))
    text2 = font.render("Temple Run", True, (0,0,0))
    text3 = font.render("Candy Crush", True, (0,0,0))
    text4 = font.render("Ludo", True, (0,0,0))
    bg.blit(text,(400,50))
    bg.blit(text2,(400,150))
    bg.blit(text3,(400,250))
    bg.blit(text4,(400,350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.update()
    if event.type == pygame.MOUSEBUTTONDOWN:
        ih = pygame.mouse.get_pos()
        pygame.draw.circle(bg, "black", ih, 15, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        aih = pygame.mouse.get_pos()
        pygame.draw.line(bg, "black", ih, aih, 5)
        pygame.draw.circle(bg, "black", aih, 15, 0)
        pygame.display.update()