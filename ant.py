import numpy as np
import pickle

class Ant():
    """
    Class for synthetic ant
    """

    def __init__(self, n_nodes, alpha=1, beta=1):

        # Naming the ant
        with open('./naming/names.txt', 'rb') as f:
            names = pickle.load(f)
        self.name = np.random.choice(names)
        print(self.name)

        # position is an integer denoting the ith row
        # in a NxN matrix describing distance between all points
        # Ant is placed on a random position in the graph by default
        self.position = np.random.choice(range(n_nodes))

        # array describing allowed subset of nodes
        self.allowed_positions = np.array([True] * n_nodes)
        self.allowed_positions[self.position] = False

        # var for tracking combined distance of ant
        self.distance_travelled = None

        # weighting parameters for pheromone strength and
        self.alpha = alpha
        #  heuristic visiblity
        self.beta = beta

    def move(self, new_position, weighted_graph_matrix):
        # moves the ant to a new node. Returns (old_pos, new_pos)
        self.distance_travelled += (
            weighted_graph_matrix[self.position, new_position]
        )
        old_position = self.position
        self.position = new_position
        self.allowed_positions[new_position] = False
        return (old_position, self.position)

    def evaluate_routes(self, graph):
        # subsets matrix the i'th row
        choice_set = graph[self.position]
        # right now it uses the same matrix for heuristic distance
        # and pheromones. it should obviously be different values
        tau = choice_set[:]**self.alpha
        eta = choice_set[:]**self.beta
        # multiplying by allowed_positions (bool)
        # to force weights of disallowed to positions to 0
        tau = tau * self.allowed_positions
        eta = eta * self.allowed_positions
        # OBS: jeg er lidt usikker på om den overvejede vej
        # skal eksluderes fra nævneren
        # OPDATERING: det returnerer sandsynligheder, så det virker korrekt.
        path_probabilities = (tau * eta) / tau.dot(eta)
        return path_probabilities

    def choose_route(self, path_probabilities):
        # returns index of chosen path
        choice = np.random.choice(
            range(len(self.allowed_positions)), p=path_probabilities
        )
        return choice

ant = Ant(10)

