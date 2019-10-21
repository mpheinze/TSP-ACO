import numpy as np
from matplotlib import pyplot as plt
import ant
import world
from record_keeper import RecordKeeper


# number of nodes on the map
N_NODES = 10
N_ANTS = 4
N_ITERATIONS = 100
RHO = 0.35
GAMMA = 2

indx_list = []
dist_list = []

# initializing world
world = world.World(N_NODES, N_ANTS, 20, RHO, GAMMA)
world.populate_world()

for j in range(N_ITERATIONS):
    for i in range(N_NODES - 1):
        world.move_ants()

    world.update_phro()

    avg_dist = world.finalize_run()

    if j % 10 == 0:
        indx_list.append(j)
        dist_list.append(avg_dist)
        print(j, avg_dist)
        world.record_keeper.render_map()
        world.record_keeper.plot_best_paths()
    world.reset_ants()

