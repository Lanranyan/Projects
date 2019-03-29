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
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        # self x and y keeps track what grid coordinate player is on

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            # '!=' not equal to
            self.vx *= 0.7071
            self.vy *= 0.7071
            # need to divide by square root of 2, or 1.414

    # def move(self, dx=0, dy=0):
    #     #lets player move in two different directions x or y
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy
    # OUT OF DATE

    def collide_with_walls(self, dir):  #dx=0, dy=0
        #will check if there's anything in the square
        #dir = direction
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False )
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False )
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y


        # for wall in self.game.walls:
        #     if wall.x == self.x + dx and wall.y == self.y + dy:
        #         #see if the wall's coordinate matches the player's
        #         return True
        #         #if true, then we tried to move into a square with
        #         # a wall, so we return True to say we did collide
        # return False
        #import  to make the False align with for

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt  #OG '= self.x * TILESIZE'
        self.y += self.vy * self.game.dt
        # dt is the timestep of the game, and can be seen on main
        # under def run. It helps move at consistent speed
        # than at a framerate
        #draws the rect at the pixel matchin it, the x * tilesize determines
        # where the upperleft hand corner of the square is drawn
        self.rect.x = self.x
        self.collide_with_walls('x')  #collides with walls in the x direction
        self.rect.y = self.y
        self.collide_with_walls('y')
        #checks wall collision for each axis
        # if pg.sprite.spritecollideany(self, self.game.walls):
        #     self.x -= self.vx * self.game.dt
        #     self.y -= self.vy * self.game.dt
        #     #undoes the movement so you don't go through wall
        #     self.rect.topleft = (self.x, self.y)


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