from settings import *
from ray import *
import pygame as pg

class Ray:
    def __init__(self, game, angle, origin):
        self.game = game
        self.origin = origin
        self.pos = pg.math.Vector2(self.origin.pos)
        self.dir = pg.math.Vector2(1, 1)
        self.angle = angle

    def update(self):
        self.update_pos()
        self.ray_cast()
    
    def update_pos(self):
        self.pos.x, self.pos.y = self.origin.pos

    def ray_cast(self):
        ray_angle = self.origin.angle - HALF_FOV + 0.0001 + math.radians(self.angle)
        self.dir.x =  self.pos.x + WIDTH * math.cos(ray_angle)
        self.dir.y = self.pos.y + WIDTH * math.sin(ray_angle)
        pg.draw.line(self.game.screen, 'red'
                    ,self.pos, (self.dir.x, self.dir.y))
    

