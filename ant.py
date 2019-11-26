#! /usr/bin/python3

import numpy as np
import pickle


class Ant():
    def __init__(self, world, n_nodes, alpha=1.0, beta=1.10):

        # initialising previous and next ant
        self.next = None
        self.n_nodes = n_nodes

        with open('./naming/names.txt', 'rb') as f:
            names = pickle.load(f)
        self.name = np.random.choice(names)

        self.position = 1
        self.distance_travelled = 0
        self.allowed_positions = np.array([True] * n_nodes)
        self.allowed_positions[self.position] = False

        self.alpha = alpha
        self.beta = beta
        self.world = world
        self.path = [1]

    def move(self):
        p = self.evaluate_routes(self.world)
        new_position = self.choose_route(p)

        # moves the ant to a new node. Returns (old_pos, new_pos)
        edge_distance = self.world.dist_matrix[self.position, new_position]
        self.distance_travelled += edge_distance

        old_position = self.position
        self.position = new_position

        self.allowed_positions[new_position] = False

        # saving path for plotting purposes
        self.path.append(self.position)

        return (old_position, self.position, edge_distance)

    def evaluate_routes(self, world):
        # subsets matrix the i'th row
        choice_set_phro = world.phro_matrix[self.position]
        choice_set_dist = world.attractiveness_matrix[self.position]

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

    def reset_ant(self):
        self.position = 1
        self.distance_travelled = 0
        self.allowed_positions = np.array([True] * self.n_nodes)
        self.allowed_positions[self.position] = False
        self.path = [1]
