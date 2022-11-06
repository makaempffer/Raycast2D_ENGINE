from ray import * 


class RayManager:
    def __init__(self, game, origin):
        self.game = game
        self.origin = origin
        self.rays = []
        self.set_rays()
    
    def set_rays(self):
        for i in range(60):
            self.rays.append(Ray(self.game, i, self.origin))

    def update(self):
        for ray in self.rays:
            ray.update()