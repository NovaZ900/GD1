import pygame

screen = pygame.display.set_mode((700,700))

pygame.init()

running = True

bg = pygame.image.load("Uno/images/space.png")
rocky = pygame.image.load("Uno/images/rocket.png")
rocky = pygame.transform.scale(rocky,(150,150))
x = 200
y = 200
img = "Uno/images/rocket2.png"

while running:
    screen.blit(bg,(0,0))
    screen.blit(rocky,(x,y))
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
            break
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    pygame.display.update()