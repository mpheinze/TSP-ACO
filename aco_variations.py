import numpy as np


class Mode():
    '''
    '''

    def __init__(self, world, *, mode='ant_system', rank_frac=1.0):
        self.mode = mode
        self.world = world
        self.rank_frac = rank_frac

        self.best_solution_dist = np.inf
        self.best_solution_path = []
        self.delta_matrix = np.zeros((self.world.n_nodes, self.world.n_nodes))

        self.mode_dict = {
            'ant_system': [self.standard_update],
            'elite_system': [self.standard_update, self.elite_update],
            'rank_system': [self.ranked_update]
        }


    def calculate_delta_matrix(self):

        for mode_func in self.mode_dict[self.mode]:
            mode_func()

        _delta_matrix = self.delta_matrix        
        self.delta_matrix = np.zeros((self.world.n_nodes, self.world.n_nodes))

        return _delta_matrix

    def _best_path(self):
        best_ant = self.world.record_keeper.top_ants[0]
        
        if best_ant.distance_travelled < self.best_solution_dist:
            self.best_solution_path = best_ant.path
            self.best_solution_dist = best_ant.distance_travelled
        
    def standard_update(self):
        ant = self.world.first_ant

        while ant.next is not None:
            distance_travelled = ant.distance_travelled

            for i, j in zip(ant.path[:-1], ant.path[1:]):
                self.delta_matrix[i, j] += self.world.gamma / distance_travelled

            ant = ant.next

    def elite_update(self):
        self._best_path()

        for i, j in zip(self.best_solution_path[:-1], self.best_solution_path[1:]):
            self.delta_matrix[i, j] += (self.world.gamma * self.world.n_ants / 50) / self.best_solution_dist

    def ranked_update(self):
        for ant in self.world.record_keeper.top_ants:
            for i, j in zip(ant.path[:-1], ant.path[1:]):
                self.delta_matrix[i, j] += (self.world.gamma * (1 / self.world.rank_frac)) / ant.distance_travelled

    