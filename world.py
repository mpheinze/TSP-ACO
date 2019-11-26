import numpy as np
import random

from ant import Ant
from node import Node
from aco_variations import Mode
from record_keeper import RecordKeeper

class World(object):
    '''

    '''

    def __init__(self, n_nodes, n_ants, xy_scale=20, alpha=1, beta=1, gamma=1, rho=1, aco_mode='ant_system', rank_frac=0.1, save_output=False):

        self.n_nodes = n_nodes
        self.n_ants = n_ants
        self.xy_scale = xy_scale
        
        # setting constants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.gamma = gamma
        self.n_top_ants = int(n_ants * rank_frac)
        self.rank_frac = rank_frac

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
        self.aco_mode = Mode(self, mode=aco_mode, rank_frac=rank_frac)

    def populate_world(self):
        first_ant = Ant(world=self, n_nodes=self.n_nodes, alpha=self.alpha, beta=self.beta)
        ant = first_ant

        for i in range(self.n_ants - 1):
            ant.next = Ant(world=self, n_nodes=self.n_nodes, alpha=self.alpha, beta=self.beta)
            ant = ant.next
        self.first_ant = first_ant

    def move_ants(self):
        ant = self.first_ant

        while ant.next is not None:
            movement = ant.move()
            ant = ant.next


    def update_phro(self):
        _delta_matrix = self.aco_mode.calculate_delta_matrix()
        self.phro_matrix = (1 - self.rho) * self.phro_matrix + _delta_matrix


    def finalize_run(self):
        _counter = 1
        ant = self.first_ant

        while ant.next is not None:
            self.record_keeper.record_distance(ant, _counter)
            ant = ant.next
            _counter += 1

    def reset_ants(self):
        ant = self.first_ant
        while ant.next is not None:
            ant.reset_ant()
            ant = ant.next
        
        self.record_keeper.avg_dist_hist.append(self.record_keeper.avg_dist)
        self.record_keeper.avg_dist = 0
