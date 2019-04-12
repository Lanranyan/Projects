import pygame as pg
from settings import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # x,y tells where to spawn
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img   # pg.Surface((TILESIZE, TILESIZE))
        # Makes the sprite a square the size of one tile
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
        #tracks how far we rotated (works same as velocity)

        # self.x = x * TILESIZE
        # self.y = y * TILESIZE
        # self x and y keeps track what grid coordinate player is on

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
            # moves in Player speed to x, but 0 in y. Move rite
            # The "-" in self.rot is to rotate in opposite dir we're pointing
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
            #we move half speed backwards

        # if self.vel.x != 0 and self.vel.y != 0:
            # '!=' not equal to
            # self.vel *= 0.7071
            # self.vx *= 0.7071
            # self.vy *= 0.7071
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
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect )
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel. y = 0
                self.hit_rect.centery = self.pos.y


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
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        # self.x += self.vx * self.game.dt  #OG '= self.x * TILESIZE'
        # self.y += self.vy * self.game.dt
        # dt is the timestep of the game, and can be seen on main
        # under def run. It helps move at consistent speed
        # than at a framerate
        #draws the rect at the pixel matchin it, the x * tilesize determines
        # where the upperleft hand corner of the square is drawn
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')  #collides with walls in the x direction
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        #checks wall collision for each axis
        self.rect.center = self.hit_rect.center

        # if pg.sprite.spritecollideany(self, self.game.walls):
        #     self.x -= self.vx * self.game.dt
        #     self.y -= self.vy * self.game.dt
        #     #undoes the movement so you don't go through wall
        #     self.rect.topleft = (self.x, self.y)

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = MOB_IMG
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        #all sprites makes sure its drawn, walls holds all wall objeccts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE