import pygame as pg
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
                #strips away any \n when looked at the file

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        # How many tiles wide and tall our map is
        # keeps track of how big our map is (width, height)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        #pixel width

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
        # the move command, when applied to rect, gives a new rect
        # that's shifted by the camera.topleft

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
            #adds half the screen size
        y = -target.rect.y + int(HEIGHT / 2)

        #Offset moves opposite from player ( if player moves right, then offset is moving left)

        # limit scrolling to map size, and keeps the player centered.
        x = min(0, x) # left
        y = min(0,y)  # top
        x = max(-(self.width - WIDTH), x)    # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        # halves the size of the screen since self.width and height are
        # double it, so 2048 - 1024

        self.camera = pg.Rect(x, y, self.width, self.height)