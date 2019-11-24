#! /usr/bin/python3

import numpy as np

from matplotlib import pyplot as plt

from world import World
from record_keeper import RecordKeeper


# number of nodes on the map
N_NODES = 15
N_ANTS = 100
N_ITERATIONS = 201

ALPHA = 1
BETA = 1
GAMMA = 1
RHO = 0.2
ACO_MODE = 'rank_system'
RANK_FRAC = 0.1


indx_list = []
dist_list = []

# initializing world
world = World(N_NODES, N_ANTS, 20, alpha=ALPHA, beta=BETA, gamma=GAMMA, rho=RHO, aco_mode=ACO_MODE, rank_frac=RANK_FRAC)

# Step 0: Populating world with nodes and ants
world.populate_world()

for j in range(N_ITERATIONS):
    
    # Step 1: Moving ants through nodes in world
    for i in range(N_NODES - 1):
        world.move_ants()

    # Step 2: calculating distances and pheromone delta levels after ant runs
    world.finalize_run()

    # Step 3: Updating pheromone level on edges
    world.update_phro()

    # Intermediary step: printing results
    print(j, world.record_keeper.avg_dist)
    if j % 100 == 0:
        world.record_keeper.plot_best_paths()

    # Step 4: Resetting ants in world
    world.reset_ants()
