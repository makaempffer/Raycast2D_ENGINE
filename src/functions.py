
def map_value(x, min_a, max_a, min_target, max_target):
    return (x - min_a) / (max_a - min_a) * (max_target - min_target) + min_target
