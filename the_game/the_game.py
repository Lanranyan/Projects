import pygame
import os
from pygame.locals import *
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        game_screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption('the_game')
        self.clock = pygame.time.Clock()

    def exit_game(self):
        for event in pygame.event.get():
            if event.type == QUIT or (
                event.type == KEYDOWN and (
                event.key == K_ESCAPE or
                event.key == K_q
                )):
                    pygame.quit()
                    quit()

class Player:
    def __init__(self):
        self.player = pygame.draw.rect(game_screen, WHITE, Rect)
        self.update()

while True:
    Game.clock.tick(FPS)
    pygame.display.update()
