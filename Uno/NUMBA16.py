import pygame

pygame.init()
HEIGHT = 700
WIDTH = 700
bg = pygame.display.set_mode((WIDTH,HEIGHT))
ih = pygame.image.load("Uno/images/VOIDbg.png")

bg.blit(ih,(0,0))

running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Uno/images/Tanko.png")
        self.image = pygame.transform.scale(self.image,(70,168))
        self.rect = self.image.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5,0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 700:
            self.rect.right = 700
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0
sprite = pygame.sprite.Group()
def start():
    aih = Player()
    sprite.add(aih)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        pressed_keys = pygame.key.get_pressed()
        aih.update(pressed_keys)
        bg.blit(pygame.image.load("Uno\images\VOIDbg.png"),(0,0))
        sprite.draw(bg)
        pygame.display.update()
start()