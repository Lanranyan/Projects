#Tilemap Demo
# https://www.youtube.com/watch?v=gbRAqFl21SA

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

# HUD functions  #heads up display
def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)
    # fill is the width, and BAR_HEIGHT is height
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # pg.key.set_repeat(500, 100)
        # hold arrow keys for 500 milisec(1/2 sec, then it
        # then it repeats every 100 mili (tenth of a second)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        #the location where our game named py is runnin,g  from
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(game_folder, 'level1.txt'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        # self.map_data = []
        # with open(path.join(game_folder, 'map.txt'), 'rt') as f:
        #     for line in f:
        #         self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        # coordinates of where you want to spawn based on the grid
        #     for x in range(10, 20):
        #         Wall(self, x, 5)
        # for row, tiles in enumerate(self.map.data):
        #     #enumerate
        #     #row = index values, tiles = strings of all charac
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         if tile == 'M':
        #             Mob(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)
        self.player = Player(self, 5, 5)
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # game loop - set self.pl aying = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
            #track the player
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # Bullet hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True,)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    def draw_grid(self):
        #draws a grid litterally
        for x in range(0, WIDTH, TILESIZE):
            #counts from zero to the width of the screen in the tilesize <-increment count by
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
            #draws a vertical line from bottom of the screen to top
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
            # draws the horizontal


    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()   ##NECESSaRY to include '()' or it won't draw
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # self.all_sprites.draw(self.screen)
        # the above code is same as the code above it  ^, it's a shortcut
        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                # if event.key == pg.K_LEFT:
                #     self.player.move(dx=-1)
                # if event.key == pg.K_RIGHT:
                #     self.player.move(dx=1)
                # if event.key == pg.K_UP:
                #     self.player.move(dy=-1)
                # if event.key == pg.K_DOWN:
                #     self.player.move(dy=1)
            #makes the player take a step every time pressed and is inefficient and choppy

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()