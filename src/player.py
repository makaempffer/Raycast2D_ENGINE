from settings import * 
import pygame as pg
import math
from functions import *


class Player():
    def __init__(self, game):
        self.game = game 
        self.pos = pg.math.Vector2(PLAYER_POS)
        self.angle = PLAYER_ANGLE
        self.dir = pg.math.Vector2(1, 1)
        self.average_point = None
        self.is_colliding = False

    def movement(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        """Make a triangle to get his angle if angle > 90 lets the ´player move away"""
        distance = None
        angle = None
        if self.average_point:
            cir_x = self.pos.x + PLAYER_SIZE * math.cos(self.angle)
            cir_y = self.pos.y + PLAYER_SIZE * math.sin(self.angle)
            #distance = math.sqrt((self.average_point.x - cir_x)**2 + (self.average_point.y - cir_y)**2)
            a = get_distance(self.pos.x, self.pos.y, self.average_point.x, self.average_point.y)
            b = get_distance(self.pos.x, self.pos.y, cir_x, cir_y)
            c = get_distance(cir_x, cir_y, self.average_point.x, self.average_point.y)
            angle = angle_triangle(a, b, c)
            #triangle = self.average_point, self.pos, (cir_x, cir_y)
            """UNNCOMMENT TO DEBUG COLLISION"""
            #pg.draw.line(self.game.screen, 'white', self.pos, self.average_point)
            #pg.draw.line(self.game.screen, 'white', self.pos, (cir_x, cir_y))
            #pg.draw.line(self.game.screen, 'white', self.average_point, (cir_x, cir_y))
            #distance2 = math.sqrt((self.average_point.x - self.pos.x)**2 + (self.average_point.y - self.pos.y)**2)
            
            #pg.draw.circle(self.game.screen, 'blue', (self.pos.x + PLAYER_SIZE * math.cos(self.angle), 
                                                    #self.pos.y + PLAYER_SIZE * math.sin(self.angle)), 5)
            #pg.draw.circle(self.game.screen, 'yellow', self.average_point, 5)
            #pg.draw.line(self.game.screen, 'yellow', self.pos, self.average_point)
            #pg.draw.line(self.game.screen, 'pink', self.average_point, (cir_x, cir_y))
        if angle and angle > 90:
            if keys[pg.K_s]:
                dx, dy = 0, 0
            if keys[pg.K_d]:
                dx, dy = 0, 0
            if keys[pg.K_a]:
                dx, dy = 0, 0
            dx, dy = dx, dy
        if angle and angle < 90 and not keys[pg.K_s]:
            dx, dy = 0, 0
        self.dir.x, self.dir.y = dx, dy
        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.pos.x , self.pos.y), 
                (self.pos.x + WIDTH * math.cos(self.angle), 
                self.pos.y + WIDTH * math.sin(self.angle)), 1)

        pg.draw.circle(self.game.screen, 'green', (self.pos.x, self.pos.y), PLAYER_SIZE, 1)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])

        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.move(self.dir.x, self.dir.y)
        self.mouse_control()

    
    def move(self, dx, dy):
        self.pos.x += dx
        self.pos.y += dy

        



