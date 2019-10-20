import numpy as np
import matplotlib.pyplot as plt
import random

import ant as ant_class
from node import Node


class World():
    def __init__(self, n_nodes, n_ants, xy_scale=20, rho=1, gamma=1):
        self.n_nodes = n_nodes
        self.n_ants = n_ants
        self.xy_scale = xy_scale
        self.rho = rho
        self.gamma = gamma

        # initializing nodes
        x = [random.randint(1, xy_scale) for i in range(n_nodes)]
        y = [random.randint(1, xy_scale) for i in range(n_nodes)]
        self.node_list = [Node(i, x[i], y[i]) for i in range(n_nodes)]

        # initialising distance matrix
        matrix = np.zeros((n_nodes, n_nodes))
        for node1 in self.node_list:
            for node2 in self.node_list:
                distance = np.sqrt(
                    (node2.x - node1.x)**2 + (node2.y - node1.y)**2)
                matrix[node1.index, node2.index] = distance

        self.dist_matrix = matrix

        # initializing pheromone matrix
        self.phro_matrix = np.ones((n_nodes, n_nodes))
        self.first_ant = None

        # container for movements. only used when plotting paths
        self.movements = []

    def populate_world(self):
        first_ant = ant_class.Ant(world=self, n_nodes=self.n_nodes)
        ant = first_ant

        for i in range(self.n_ants - 1):
            ant.next = ant_class.Ant(world=self, n_nodes=self.n_nodes)
            ant = ant.next
        self.first_ant = first_ant

    def move_ants(self, collect_movements=False):
        ant = self.first_ant
        phro_delta = np.zeros(shape=(self.phro_matrix.shape))

        while ant.next is not None:
            movement = ant.move()
            phro_delta[movement[0], movement[1]] += self.gamma / movement[2]
            ant = ant.next
            if collect_movements is True:
                self.movements.append(movement)

        self.phro_delta = phro_delta

    def update_phro(self):
        self.phro_matrix = (1 - self.rho) * self.phro_matrix + self.phro_delta

    def finalize_run(self):
        ant = self.first_ant
        dist_sum = 0

        while ant.next is not None:
            dist_sum += ant.distance_travelled

            ant.reset_ant()
            ant = ant.next

        avg_distance = dist_sum / self.n_ants
        return avg_distance

    # def plot_movements(self):
    #     fig, ax = plt.subplots()
    #     plt.scatter(
    #         x=[node.x for node in self.node_list],
    #         y=[node.x for node in self.node_list]
    #     )
    #     self.movements
