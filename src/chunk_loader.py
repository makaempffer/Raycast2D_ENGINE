from chunks import ChunkMap, mini_map
from settings import *
from pygame import Vector2
class ChunkLoader:
    def __init__(self, origin):
        self.chunks = []
        self.player = origin
        self.parent_chunk = None
        self.load_chunks()
        self.get_parent_chunk()
        self.loaded_chunks = []

    def update(self):
        self.get_parent_chunk()
        self.get_loaded_chunks()

    def get_parent_chunk(self):
        player_pos = self.player.pos
        if player_pos == (0, 0):
            self.parent_chunk_pos = (0, 0)
            return
        parent_chunk_pos_x = math.floor(player_pos.x // CHUNK_SIZE)
        parent_chunk_pos_y = math.floor(player_pos.y // CHUNK_SIZE)
        self.parent_chunk = self.chunks[parent_chunk_pos_x][parent_chunk_pos_y]
        
    def get_loaded_chunks(self) -> list: 
        loaded_chunks = []
        for row in self.chunks:
            for chunk in row:
                for border in chunk.block_borders:
                    loaded_chunks.append(border)
        self.loaded_chunks = loaded_chunks
        return loaded_chunks
#FIX THIS
    def load_chunks(self):
        w, h = 10, 10
        array = [[ChunkMap(CHUNK_SIZE, (x * CHUNK_SIZE, y * CHUNK_SIZE), mini_map) for x in range(w)] for y in range(h)]
        self.chunks = array



