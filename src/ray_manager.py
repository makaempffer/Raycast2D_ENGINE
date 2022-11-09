from ray import * 
from functions import *

class RayManager:
    def __init__(self, game, origin, walls: list, renderer):
        self.game = game
        self.objects = walls
        self.renderer = renderer
        self.origin = origin
        self.rays = []
        self.collision_rays = []
        self.radians = [round(math.pi/6, 1), round(math.pi/4, 1), round(math.pi/3, 1), round(math.pi/2, 1)]
        self.set_rays()
    
    def set_rays(self):
        """Create ray array and set angles to ++DELTA_ANGLE"""
        angle = DELTA_ANGLE
        for i in range(NUM_RAYS):
            self.rays.append(Ray(self.game, angle, self.origin, i))
            angle += DELTA_ANGLE
        # COLLISION RAYS EVERY RADIANS / 9 ARRAY MAKING
        #angles = [0, math.pi / 6, math.pi/4, math.pi / 3, math.pi/2, 3 * (math.pi) / 4, 5 * math.pi / 6, math.pi, 5 * (math.pi) / 4,
                    #3 * (math.pi) / 2, 7 * (math.pi) / 4]
        #for angle in angles:
            #self.collision_rays.append(Ray(self.game, angle, self.origin, i))
        
        for i in range(0, 360, 10):
            self.collision_rays.append(Ray(self.game.screen, math.radians(i), self.origin, i, PLAYER_SIZE))


    def update(self):
        self.cast_collision_rays()
        self.cast_rays()
    
    def cast_collision_rays(self):
        """get the direction of movement of the player and the closest rays colliding,
        if the direction of the player is in one of those directions multiply it by -1"""
        colliding_rays = []
        
        for ray in self.collision_rays:
            average_vector = 0, 0
            ray.update()
            closest_object = None
            record = 100000
            for object in self.objects:
                if pg.math.Vector2.distance_to(self.origin.pos, pg.Vector2(object[0], object[1])) > MAX_OBJECT_LENGHT:
                    continue
                point = ray.cast(object[0], object[1])
                if point:
                    
                    point_x, point_y = point  
                    distance_from_object =  math.sqrt((point_x - ray.pos.x)**2 + (point_y - ray.pos.y)**2)
                    
                    if distance_from_object < record:
                        record = distance_from_object
                        closest_object = point

            if closest_object:
                #uncomment to see collision rays
                #pg.draw.line(self.game.screen, 'red', ray.pos, closest_object)
                if record < PLAYER_SIZE:
                    ray_pos = pg.math.Vector2(closest_object)
                    colliding_rays.append(ray_pos)

            collided = False
            colliding_rays_num = 0

            for collision in colliding_rays:
                dx = abs(collision.x - self.origin.pos.x)
                dy = abs(collision.y - self.origin.pos.y)
                Radius = PLAYER_SIZE

                if dx < Radius and dy < Radius:
                    colliding_rays_num += 1
                    average_vector += collision / len(colliding_rays)
                    #uncomment to see collision points
                    #pg.draw.circle(self.game.screen, 'red', collision, 5) 
                    collided = True

            if collided:
                self.origin.is_colliding = True
                self.origin.average_point = average_vector
                
            if colliding_rays_num < 1:
                self.origin.is_colliding = False
                self.origin.average_point = None
                collided = False
            

    def cast_rays(self):
        """Updates renderer to draw <list> by casting rays 
        returning positions and columns number"""
        columns = []
        visible_objects = []
        for ray in self.rays:
            ray.update()
            closest_object = None
            record = 100000
            for object in self.objects:
                obj_vect = pg.Vector2(object[0], object[1])
                #if an object is > 800 away it wont process 
                if pg.math.Vector2.distance_to(self.origin.pos, obj_vect) > 1015:
                    continue
                point = ray.cast(object[0], object[1])
                if point:
                    point_x, point_y = point  
                    distance_from_object =  math.sqrt((point_x - ray.pos.x)**2 + (point_y - ray.pos.y)**2)
                    
                    if distance_from_object < record:
                        record = distance_from_object
                        closest_object = point
                        #new code
                        visible_objects.append(closest_object)
                        columns.append(ray.column)

                        
            #only setting the objects if render distance is met
            #if closest_object and record < RENDER_DISTANCE - 1:
                #visible_objects.append(point)
                #columns.append(ray.column)
                #pg.draw.line(self.game.screen, 'blue', ray.pos, (closest_object))
                #objects.append(closest_object)
                #columns.append(ray.column)
            #debbugging amount of visible objects vs objects
            #print("visible objects=",len(visible_objects), "objects=", len(objects))
        self.renderer.objects = visible_objects
        self.renderer.columns = columns