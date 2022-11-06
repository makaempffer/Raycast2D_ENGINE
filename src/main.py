import pygame as pg
import sys
from settings import * 
from player import * 
from world_object_manager import * 
from ray import *
from ray_manager import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
            self.player = Player(self)
            self.world_object_manager = WorldObjectManager(self)
            self.world_object_manager.add_random_object_number(5)
            self.ray_manager = RayManager(self, self.player)

    def update(self):
        #updates modules
        self.player.update()
        self.ray_manager.update()
        ################
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        #2D render
        self.screen.fill('black')
        self.player.draw()
        self.world_object_manager.draw()



    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
                

if __name__ == '__main__':
    game = Game()
    game.run()
    