import numpy as np
from record_keeper import RecordKeeper
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
        self.attractiveness_matrix = (1 / self.dist_matrix)
        np.fill_diagonal(self.attractiveness_matrix, 0)

        # initializing pheromone matrix
        self.phro_matrix = np.ones((n_nodes, n_nodes))
        self.delta_matrix = np.zeros((n_nodes, n_nodes))
        
        self.first_ant = None

        # initialising record_keeper
        self.record_keeper = RecordKeeper(self)

    def populate_world(self):
        first_ant = ant_class.Ant(world=self, n_nodes=self.n_nodes)
        ant = first_ant

        for i in range(self.n_ants - 1):
            ant.next = ant_class.Ant(world=self, n_nodes=self.n_nodes)
            ant = ant.next
        self.first_ant = first_ant

    def move_ants(self):
        ant = self.first_ant

        while ant.next is not None:
            movement = ant.move()
            ant = ant.next


    def update_phro(self):
        self.phro_matrix = (1 - self.rho) * self.phro_matrix + self.delta_matrix
        self.delta_matrix = np.zeros(shape=(self.n_nodes, self.n_nodes))


    def finalize_run(self):
        ant = self.first_ant
        dist_sum = 0

        while ant.next is not None:
            distance_travelled = ant.distance_travelled

            for i, j in zip(ant.path[:-1], ant.path[1:]):
                self.delta_matrix[i, j] += self.gamma / distance_travelled

            dist_sum += distance_travelled
            self.record_keeper.record_distance(distance_travelled, ant)

            ant = ant.next

        avg_distance = dist_sum / self.n_ants
        return avg_distance

    def reset_ants(self):
        ant = self.first_ant
        while ant.next is not None:
            ant.reset_ant()
            ant = ant.next
