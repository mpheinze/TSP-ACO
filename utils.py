import numpy as np

# calculating euclidian distance between two points
def euclidian_distance(p, q):    
    return np.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)    

# generate distance matrix from list of data points
def distance_matrix(node_list):
    n_nodes = len(node_list)
    matrix = np.zeros((n_nodes, n_nodes))

    for idx1, node1 in enumerate(node_list):
        for idx2, node2 in enumerate(node_list):
            distance = euclidian_distance(node1, node2)
            matrix[idx1, idx2] = distance

    return matrix