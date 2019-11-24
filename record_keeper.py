import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


class RecordKeeper(object):
    """
    
    """

    def __init__(self, world):

        self.nodes_x = np.array([node.x for node in world.node_list])
        self.nodes_y = np.array([node.y for node in world.node_list])

        self.world = world

        # matrix for keeping track of ant movements
        self.movement_matrix = np.zeros(shape=(world.n_nodes, world.n_nodes))

        self.top_ant_dists = np.zeros(self.world.n_top_ants)
        self.top_ants = [None] * self.world.n_top_ants

        self.avg_dist = 0

        self.axes = None

    def record_distance(self, ant, ant_counter):
        # if 0 is greater than the minimum value, then the new distance
        # is larger than whatever distances are currently set as best
        # thus earning it a spot

        self.avg_dist += 1 / (ant_counter) * (ant.distance_travelled - self.avg_dist)

        differences = (self.top_ant_dists - ant.distance_travelled)
        if 0 > differences.min():

            # inserting new ant in list
            self.top_ants.insert(differences.argmin(), ant)
            # popping worst ant from list
            self.top_ants.pop()

            # setting new top distances
            for i in range(len(self.top_ants)):
                try:
                    self.top_ant_dists[i] = self.top_ants[i].distance_travelled
                except AttributeError:
                    pass
        else:
            pass
        return None

    def render_map(self):
        fig, axes = plt.subplots()
        axes.scatter(
            x=self.nodes_x,
            y=self.nodes_y,
        )
        self.axes = axes

    def plot_best_paths(self):
        self.render_map()
        for ant in self.top_ants[:3]:
            x = [self.nodes_x[i] for i in ant.path]
            y = [self.nodes_y[i] for i in ant.path]
            print(f'Path: {ant.path}')
            self.axes.plot(x, y)
            self.axes.text(self.nodes_x[1], self.nodes_y[1], 'Start')
        plt.show()
