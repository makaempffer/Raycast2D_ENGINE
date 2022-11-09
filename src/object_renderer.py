from settings import *
import pygame as pg
from functions import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.objects = []
        self.columns = []
    
    def render(self):
        """Draws a rect in the position of the ray column that hit(scaled), in center of the screen - calculated height"""
        for i, object in enumerate(self.objects):
            #USEFULL DATA#
            object_vect = pg.Vector2(object)
            player_vect = pg.Vector2(self.game.player.pos)
            dist_to_object = pg.math.Vector2.distance_to(player_vect, object_vect)
            projection_height = OBJECT_HEIGHT / dist_to_object * SCREEN_DIST
            color = map_value(dist_to_object, 0, WIDTH, 0, 255)
            color = color, color, color
            #IMPORTANT DATA#
            pg.draw.rect(self.game.screen, color, (self.columns[i] * SCALE, HALF_HEIGHT - projection_height / 2, SCALE, projection_height))
        


