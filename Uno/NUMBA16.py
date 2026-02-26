import pygame

pygame.init()
bg = pygame.display.set_mode((700,700))
ih = pygame.image.load("Uno\images\VOIDbg.png")

bg.blit(ih,(0,0))

running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Uno\images\Tanko.png")
        self.image = pygame.transform.scale(self.image,(115,70))
        self.rect = self.image.get_rect(14,23)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.update()