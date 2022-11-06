import pygame as pg


class WorldObject():
    def __init__(self, game, a: tuple, b: tuple):
        self.game = game
        self.a_x, self.a_y = a
        self.b_x, self.b_y = b 
    
    def draw(self):
        pg.draw.line(self.game.screen, 'white',
                    (self.a_x, self.a_y), 
                    (self.b_x, self.b_y), 1)