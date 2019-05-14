# https://www.digitalocean.com/community/tutorials/how-to-install-pygame-and-create-a-template-for-developing-games-in-python-3
# https://sivasantosh.wordpress.com/2012/07/16/pygame-template/
# https://gist.github.com/MatthewJA/7544830
# https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3

import pygame
from pygame.locals import *

pygame.init()
# init = initialize - starts up all pygame modules
# pygame.font.init()
# https://www.pygame.org/docs/ref/font.html

# i = pygame.init()
# print(i)

# f = pygame.font.init()
# print(f)

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
# (800, 600) is a tuple as argumuent to set_mode()

pygame.display.update()
# updates portions of the screen, flip updates all