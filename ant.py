import numpy as np
import pickle

from world import World
# import world
# from world import World

class Ant():
    """
    Class for synthetic ant
    """

    def __init__(self, world, n_nodes, alpha=1, beta=1):

        # initialising previous and next ant
        self.next = None
        # Naming the ant
        with open('./naming/names.txt', 'rb') as f:
            names = pickle.load(f)
        self.name = np.random.choice(names)
        print(self.name)

        # position is an integer denoting the ith row
        # in a NxN matrix describing distance between all points
        # Ant is placed on a random position in the graph by default
        self.position = 1

        # array describing allowed subset of nodes
        self.allowed_positions = np.array([True] * n_nodes)
        self.allowed_positions[self.position] = False

        # var for tracking combined distance of ant
        self.distance_travelled = 0

        # weighting parameters for pheromone strength and
        self.alpha = alpha
        #  heuristic visiblity
        self.beta = beta

    def move(self):
        p = self.evaluate_routes(self.world)
        new_position = self.choose_route(p)
        # moves the ant to a new node. Returns (old_pos, new_pos)
        edge_distance = weighted_graph_matrix[self.position, new_position]
        self.distance_travelled += edge_distance
        
        old_position = self.position
        self.position = new_position

        self.allowed_positions[new_position] = False
        return (old_position, self.position, edge_distance)

    def evaluate_routes(self, world):
        # subsets matrix the i'th row
        choice_set_phro = world.phro_matrix[self.position]
        choice_set_dist = world.dist_matrix[self.position]
        # right now it uses the same matrix for heuristic distance
        # and pheromones. it should obviously be different values
        tau = choice_set_phro**self.alpha
        eta = choice_set_dist**self.beta
        # multiplying by allowed_positions (bool)
        # to force weights of disallowed to positions to 0
        tau = tau * self.allowed_positions
        eta = eta * self.allowed_positions

        path_probabilities = (tau * eta) / tau.dot(eta)
        return path_probabilities

    def choose_route(self, path_probabilities):
        # returns index of chosen path
        choice = np.random.choice(
            range(len(self.allowed_positions)), p=path_probabilities
        )
        return choice