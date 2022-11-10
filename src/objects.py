from pygame import Vector2

class WallRect:
    """Object that represent a rectangle shape made of <lines>"""
    def __init__(self, startpos: tuple, width: int, height: int):
        self.start_pos = Vector2(startpos)
        self.width = width
        self.height = height
        self.borders = self.get_borders()

    
    def get_borders(self) -> list:
        """Returns a <list> of all border coordinates"""
        borders = [None, None, None, None]
        borders[0] = (self.start_pos.x, self.start_pos.y), (self.start_pos.x + self.width, self.start_pos.y)
        borders[1] = (self.start_pos.x, self.start_pos.y), (self.start_pos.x, self.start_pos.y + self.height)
        borders[2] = (self.start_pos.x, self.start_pos.y + self.height), (self.start_pos.x + self.width, self.start_pos.y + self.height)
        borders[3] = (self.start_pos.x + self.width, self.start_pos.y + self.height), (self.start_pos.x + self.width, self.start_pos.y)
        return borders
    

        