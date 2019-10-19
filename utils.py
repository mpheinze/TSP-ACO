import numpy as np

# calculating euclidian distance between two points
def euclidian_distance(p, q):    
    return np.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)