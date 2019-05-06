import pygame as pg
import pytmx
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

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

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        # load_pygame is there because pytmx is just for reading tiled maps, not using pygame
        # pixelalpha = True ensures the transparency of our tiles and tilemap
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    # takes a surface and draws all our tiles on it in the
    # order the layers are in, so ground then walls...
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        # gid means global identifier to read the tiles by finding its image
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                # in tiled, there are 3 layers: ^ Tile, Object, Image
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))
    # creates a surface to draw map onto
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    # applies offset to sprite
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
        # the move command, when applied to rect, gives a new rect
        # that's shifted by the camera.topleft

    # applies offset to rectangle
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
            #adds half the screen size
        y = -target.rect.centery + int(HEIGHT / 2)

        #Offset moves opposite from player ( if player moves right, then offset is moving left)

        # limit scrolling to map size, and keeps the player centered.
        x = min(0, x) # left
        y = min(0,y)  # top
        x = max(-(self.width - WIDTH), x)    # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        # halves the size of the screen since self.width and height are
        # double it, so 2048 - 1024

        self.camera = pg.Rect(x, y, self.width, self.height)