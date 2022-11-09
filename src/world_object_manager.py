from objects import * 
from settings import *
import random


class WorldObjectManager:
    def __init__(self, game):
        self.game = game
        self.objects_rects = []
        self.objects_rects_borders = []
    
    def add_rect(self, rect: WallRect):
        self.objects_rects.append(rect)
    
    def add_random_rects(self, number: int):
        """Add a <int> random_pos <WallRect> and store borders in <list>"""
        for i in range(number):
            self.add_rect(WallRect(self.game, (random.randint(0, WIDTH), (random.randint(0, HEIGHT))), 100, 500))
            for border in self.objects_rects[i].borders:
                self.objects_rects_borders.append(border)

    def draw(self):
        for wall in self.objects_rects:
            wall.draw()