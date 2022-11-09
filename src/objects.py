from pygame import draw, Vector2

class Wall:
    def __init__(self, game, a: tuple, b: tuple):
        self.game = game
        self.a_x, self.a_y = a
        self.b_x, self.b_y = b 
    
    def draw(self):
        draw.line(self.game.screen, 'gray',
                    (self.a_x, self.a_y), 
                    (self.b_x, self.b_y), 1)


class WallRect:
    """Object that represent a rectangle shape made of <lines>"""
    def __init__(self, game, startpos: tuple, width: int, height: int):
        self.game = game
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
    

    def draw(self):
        draw.line(self.game.screen, 'white', self.start_pos, (self.start_pos.x + self.width, self.start_pos.y))
        draw.line(self.game.screen, 'white', self.start_pos, (self.start_pos.x, self.start_pos.y + self.height))
        draw.line(self.game.screen, 'white', (self.start_pos.x, self.start_pos.y + self.height), (self.start_pos.x + self.width, self.start_pos.y + self.height))
        draw.line(self.game.screen, 'white',  (self.start_pos.x + self.width, self.start_pos.y + self.height), (self.start_pos.x + self.width, self.start_pos.y))
        