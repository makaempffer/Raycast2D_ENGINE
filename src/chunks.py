from map import *
from objects import *
from settings import *

class ChunkMap:
    def __init__(self, chunk_size: int = CHUNK_SIZE, pos = (0, 0) , layout = mini_map):
        self.size = chunk_size
        self.pos = pos
        self.layout = layout
        self.block_positions = []
        self.block_objects = []
        self.block_borders = []
        self.set_chunk_blocks()
        self.get_borders()

    def set_chunk_blocks(self):
        for j, row in enumerate(self.layout):
            for i, value in enumerate(row):
                if value:
                    self.block_positions.append((self.pos[0] + i * 100, self.pos[1] + j * 100))
    
    def get_borders(self):
        for i, start_pos in enumerate(self.block_positions):
            self.block_objects.append(WallRect(start_pos, 100, 100))
            for border in self.block_objects[i].borders:
                self.block_borders.append(border)
