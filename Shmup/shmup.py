# Shmup game
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
AKA = (212, 1, 8)
GREEN = (0, 255, 0)
GREEN2 = (51, 255, 28)
LIME = (142, 255, 28)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MANGO = (255, 153, 0)
LIYELLOW = (255, 249, 41)
PURPLE = (205, 0, 255)
PASTPURP  = (213, 181, 255)
PASTPINK = (255, 193, 218)
SAND = (255, 229, 193)
PASTGREN = (193, 255, 212)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Schmup!")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #must call forth this sprite function so sprites work
        #1. call function, 2. create image, 3. fill it, 4. def a rect
        #5. Center and position it, 6) create speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(MANGO)
        self.rect = self.image.get_rect()
        # Centers the rect in the screen by ' / 2 '
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0  # 0 = shouldn't be moving until key pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        # Tells the rect to move at its current speed
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()