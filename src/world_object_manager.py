from world_object import WorldObject 
from settings import *
import random



class WorldObjectManager:
    def __init__(self, game):
        self.game = game
        self.wall_list = []
    
    def add_object(self, object: WorldObject) -> None:
        self.wall_list.append(object)
    
    def add_random_object(self):
        self.wall_list.append(WorldObject(self.game, (random.randint(0, WIDTH), random.randint(0, HEIGHT)), (random.randint(0, WIDTH),random.randint(0, HEIGHT))))
    
    def add_random_object_number(self, number):
        for i in range(number):
            self.add_random_object()

    def draw(self):
        for object in self.wall_list:
            object.draw()
