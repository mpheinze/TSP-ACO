import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


class RecordKeeper(object):
    """docstring for RecordKeeper"""

    def __init__(self, world):

        self.nodes_x = np.array([node.x for node in world.node_list])
        self.nodes_y = np.array([node.y for node in world.node_list])

        # matrix for keeping track of ant movements
        self.movement_matrix = np.zeros(shape=(world.n_nodes, world.n_nodes))

        self.top_ant_dists = np.array([0, 0, 0])
        self.top_ants = [None, None, None]

        self.axes = None

    def render_map(self):
        fig, axes = plt.subplots()
        axes.scatter(
            x=self.nodes_x,
            y=self.nodes_y,
        )
        self.axes = axes

    def record_distance(self, distance_travelled, ant):
        # if 0 is greater than the minimum value, then the new distance
        # is larger than whatever distances are currently set as best
        # thus earning it a spot
        differences = (self.top_ant_dists - distance_travelled)
        if 0 > differences.min():

            # inserting new ant in list
            self.top_ants.insert(differences.argmin(), ant)
            # popping worst ant from list
            self.top_ants.pop()

            # setting new top distances
            for i in range(3):
                try:
                    self.top_ant_dists[i] = self.top_ants[i].distance_travelled
                except AttributeError:
                    pass
        else:
            pass
        return None

    def plot_best_paths(self):
        for ant in self.top_ants:
            print(ant.path)
            x = [self.nodes_x[i] for i in ant.path]
            y = [self.nodes_y[i] for i in ant.path]
            self.axes.plot(x, y)
            self.axes.text(self.nodes_x[1], self.nodes_y[1], 'Start')
        plt.show()
