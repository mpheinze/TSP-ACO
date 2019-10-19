import numpy as np
import random

import ant as antclass
# import ant
# from ant import Ant

class World():
    def __init__(self, n_nodes, n_ants, xy_scale=20, rho=1, gamma=1):
        self.n_nodes = n_nodes
        self.n_ants = n_ants
        self.xy_scale = xy_scale
        self.rho = rho
        self.gamma = gamma

        # initializing distance matrix
        x = [random.randint(1, xy_scale) for i in range(n_nodes)]
        y = [random.randint(1, xy_scale) for i in range(n_nodes)]
        
        node_list = list(zip(x, y))
        matrix = np.zeros((n_nodes, n_nodes))

        for idx1, node1 in enumerate(node_list):
            for idx2, node2 in enumerate(node_list): 
                distance = np.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)
                matrix[idx1, idx2] = distance
        
        self.dist_matrix = matrix
    
        # initializing pheromone matrix
        self.phro_matrix = np.ones((n_nodes, n_nodes))

        self.first_ant = None


    def populate_world(self):
        first_ant = antclass.Ant(world = self, n_nodes = self.n_nodes)
        ant = first_ant

        for i in range(self.n_ants - 1):
            ant.next = antclass.Ant(world = self, n_nodes = self.n_nodes)
            ant = ant.next
        self.first_ant = first_ant
    

    def move_ants(self):
        ant = self.first_ant
        # 0 initialised matrix with identical shape to phro_matrix
        # to collect delta tau's
        phro_delta = np.zeros(shape = (self.phro_matrix.shape))        
        while ant.next is not None:
            movement = ant.move()
            phro_delta[movement[0], movement[1]] += self.gamma / movement[2]
            ant = ant.next

        self.phro_delta = phro_delta

    def update_phro(self):
        self.phro_matrix_decay = (1 - self.rho) * self.phro_matrix + self.phro_delta

    def avg_distance_travelled(self):
        
        ant = self.first_ant

        dist_sum = 0
        while ant.next is not None:
            dist_sum += ant.distance_travelled
            ant = ant.next

        avg_distance = dist_sum / self.n_ants
        return avg_distance