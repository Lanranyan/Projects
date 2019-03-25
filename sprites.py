import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # x,y tells where to spawn
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        # Makes the sprite a square the size of one tile
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x
        self.y = y
        # self x and y keeps track what grid coordinate player is on

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.vx = -PLAYER_SPEED
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vx = PLAYER_SPEED

    def move(self, dx=0, dy=0):
        #lets player move in two different directions x or y
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        #will check if there's anything in the square
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                #see if the wall's coordinate matches the player's
                return True
                #if true, then we tried to move into a square with
                # a wall, so we return True to say we did collide
        return False
        #import  to make the False align with for

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt        #OG '= self.x * TILESIZE'
        self.y += self.vy * self.game.dt
        # dt is the timestep of the game, and can be seen on main
        # under def run. It helps move at consistent speed
        # than at a framerate
        #draws the rect at the pixel matchin it, the x * tilesize determines
        # where the upperleft hand corner of the square is drawn
        self.rect.topleft = (self.x, self.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        #all sprites makes sure its drawn, walls holds all wall objeccts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE