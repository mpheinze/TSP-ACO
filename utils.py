import random
import numpy as np
import pandas as pd

# calculating euclidian distance between two points
def euclidian_distance(p, q):    
    return np.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)    

# generate distance matrix from list of data points
def distance_matrix(point_list):
    n_points = len(point_list)
    matrix = np.zeros((n_points, n_points))

    for idx1, point1 in enumerate(point_list):
        for idx2, point2 in enumerate(point_list):
            distance = euclidian_distance(point1, point2)
            matrix[idx1, idx2] = distance

    return matrix