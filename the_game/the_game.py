# https://www.digitalocean.com/community/tutorials/how-to-install-pygame-and-create-a-template-for-developing-games-in-python-3
# https://sivasantosh.wordpress.com/2012/07/16/pygame-template/
# https://gist.github.com/MatthewJA/7544830
# https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3

import pygame
from pygame.locals import *
# evokes stuff like event.type w/o pygame. in front

pygame.init()
# init = initialize - starts up all pygame modules
# pygame.font.init()
# https://www.pygame.org/docs/ref/font.html

# i = pygame.init()
# print(i)
### Returns a tuple where x = successful pygame initializations and y = # of failures

# f = pygame.font.init()
# print(f)
### f returning None = the module isn't available within this particular environment

# GAME SURFACE

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
# (800, 600) is a tuple as argumuent to set_mode()

pygame.display.update()
# updates portions of the screen, flip updates all

# GAME LOOP
while True:

def event_handler():
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT or (
            event.type == KEYDOWN and (
            event.key == K_ESCAPE or
            event.key == K_q
            )):
            pygame.quit()
            # uninitializes the pygame modules within pygame
            quit()
            # exits the program


