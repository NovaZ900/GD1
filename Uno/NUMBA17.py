import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()
HEIGHT = 800
WIDTH = 1000
bg = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GALACTIC SHOWDOWN")
pygame.display.set_icon("Uno/images/SHIPICON.png")
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

ORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
SPACEWIDTH = 55
SPACEHEIGHT = 40
HEALTH = pygame.font.SysFont("Comic Sans", 40)
WINNER = pygame.font.SysFont("Comic Sans", 100)

ih = pygame.transform.scale(pygame.image.load(os.path.join("images","PlayerShip.png")),(WIDTH, HEIGHT))
aih = pygame.transform.scale(pygame.image.load(os.path.join("images","Enemy.png")),(WIDTH, HEIGHT))

class Ship(pygame.sprite.Sprite):
    def __init___(self,image,x,y,controls,boundary):
        super.__init__()
        self.image = image
        self.controls = controls
        self.boundary = boundary
        self.rect = self.image.get_rect(top_left = (x,y))
        self.health = 200
        self.bullets = pygame.sprite.Group()
    
    def update(self,keys):
        if keys[self.control["left"]] and self.rect.left > self.boundary[0]:
            self.rect.x -= VEL
        if keys[self.control["right"]] and self.rect.right < self.boundary[0]:
            self.rect.x += VEL
        if keys[self.control["up"]] and self.rect.top > 0:
            self.rect.y -= VEL
        if keys[self.control["down"]] and self.rect.bottom < HEIGHT-15:
            self.rect.y += VEL
    
    def shoot(self,direction):
        if len(self.bullets) < MAX_BULLETS:
            bullet = Bullet(self.rect, direction)
            self.bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,shiprect,direction):
        super.__init__()
        self.image = pygame.Surface(10,5)
        self.rect = self.image.get_rect(center = (shiprect.centerx,shiprect.centery))
        self.direction = direction
    def update(self):
        self.rect.x += BULLET_VEL * self.direction
        if self.rect.right < 0 or self.rect.lect > WIDTH:
            self.kill()

def draw_window(RED,BLUE):
    bg.blit("Uno/images/space.png",(0,0))
    pygame.draw.rect(bg, "white", ORDER)
    RED_health = HEALTH.render(f"HP: {RED.health}", 1, "white")
    BLUE_health = HEALTH.render(f"HP: {BLUE.health}", 1, "white")
    bg.blit(RED_health, (WIDTH - RED_health.get_width() - 10, 10))
    bg.blit(BLUE_health, (10, 10))
    bg.blit(RED.image,RED.rect)
    bg.blit(BLUE.image,BLUE.rect)
    RED.bullet.draw(bg)
    BLUE.bullet.draw(bg)
    pygame.display.update()

def draw_winner(text):
    winner = WINNER.render(text,1, "white")
    bg.blit(winner,(WIDTH//2 - winner.get_width()//2,HEIGHT//2 - winner.get_height()//2))
    pygame.display.update()
    pygame.time.delay(4000)

def GAME():
    global boundary
    clock = pygame.time.Clock()
    red_controls = {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "up": pygame.K_UP,
        "down": pygame.K_DOWN
    }
    blue_controls = {
        "left": pygame.K_a,
        "right": pygame.K_d,
        "up": pygame.K_w,
        "down": pygame.K_s
    }

    RED = Ship(ih, 700, 300, red_controls, (boundary.right,WIDTH))
    BLUE = Ship(aih, 100, 300, blue_controls, (0, boundary.left))
    all_sprites = pygame.sprite.Group(RED,BLUE)
running = True
while running:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
            break