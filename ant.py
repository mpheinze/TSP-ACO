import numpy as np
import pickle


class Ant():
    """
    Class for synthetic ant
    
    """

    def __init__(self, n_nodes, alpha, beta):

        # Naming the ant
        with open('names.txt', 'rb') as f:
            names = pickle.load(f)
        self.name = np.random.choice(names)

        # position is an integer denoting the ith row
        # in a NxN matrix describing distance between all points
        # Ant is placed on a random position in the graph by default
        self.position = np.random.choice(range(1, n_nodes))

        # array describing allowed subset of nodes
        self.allowed_positions = np.array([True] * n_nodes)
        self.allowed_positions[self.position] = False

        # var for tracking combined distance of ant
        self.distance_travelled = None

        # weighting parameters for heuristic visiblity and
        self.alpha = alpha
        # pheromone strength
        self.beta = beta

    def move(self, new_position, weighted_graph_matrix):
        self.distance_travelled += (
            weighted_graph_matrix[self.position, new_position]
        )
        self.position = new_position
        self.allowed_positions[new_position] = False

    def evaluate_routes(self, weighted_graph_matrix):
        choice_set = weighted_graph_matrix[self.position]
