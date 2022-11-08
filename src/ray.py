from settings import *
from ray import *
import pygame as pg

class Ray:
    def __init__(self, game, angle, origin, column):
        self.game = game
        self.origin = origin
        self.pos = pg.math.Vector2(self.origin.pos)
        self.dir = pg.math.Vector2(1, 1)
        self.angle = angle
        self.column = column

    def update(self):
        self.update_pos()
        self.update_ray_direction()
    
    def update_pos(self):
        self.pos.x, self.pos.y = self.origin.pos

    def update_ray_direction(self):
        """Updates the ray direction depending on the angle given"""
        ray_angle = self.origin.angle - HALF_FOV + 0.0001 + self.angle
        self.dir.x =  self.pos.x + WIDTH * math.cos(ray_angle)
        self.dir.y = self.pos.y + WIDTH * math.sin(ray_angle)
        #draw a line in direction of the ray
        #pg.draw.line(self.game.screen, 'red'
                    #,self.pos, (self.dir.x, self.dir.y))

    def cast(self, wall) -> tuple:
        """Casts a ray that checks for interception with a line 
        and return the point of interception as a tuple
        [-] Called from the ray manager for each ray"""
        x1 = wall.a_x
        x2 = wall.b_x
        y1 = wall.a_y
        y2 = wall.b_y
        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.dir.x
        y4 = self.dir.y #+ self.offset

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if t > 0 and t < 1 and u > 0:
            intersection_point_x = x1 + t * (x2 - x1)
            intersection_point_y = y1 + t * (y2 - y1)
            #draws a circle in the intersection points
            #pg.draw.circle(self.game.screen, 'green', (intersection_point_x, intersection_point_y), 5)
            return (intersection_point_x, intersection_point_y)
        else:
            return
        
    def is_colliding(self, distance):
        if distance < PLAYER_SIZE:
            return True
        else:
            return False
