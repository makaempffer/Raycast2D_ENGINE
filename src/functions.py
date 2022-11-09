import math
def map_value(x, min_a, max_a, min_target, max_target):
    return (x - min_a) / (max_a - min_a) * (max_target - min_target) + min_target

def angle_between_vectors(a, b, c, d):
    dot_product = a * c + b * d
    mod_vec_1 = math.sqrt(a * a + b * b) * math.sqrt(c * c + d * d)
    angle = dot_product / mod_vec_1
    return angle