#! /usr/bin/python3

import numpy as np

from matplotlib import pyplot as plt
from record_keeper import RecordKeeper
from world import World
from utils import get_output_path

##### ---------- adjust parameters here ---------- #####

# world parameters
N_NODES = 15
N_ANTS = 200
N_ITERATIONS = 1000

# algorithm parameters
ALPHA = 1
BETA = 1
GAMMA = 1
RHO = 0.2

# mode parameters
ACO_MODE = 'elite_system'
RANK_FRAC = 0.1

# plotting parameters
SAVE_OUTPUT = True
N_PLOTS = 10

##### -------------------------------------------- #####


indx_list = []
dist_list = []
plot_steps = np.linspace(1, N_ITERATIONS - 1, N_PLOTS, dtype=int)
plot_path = get_output_path() if SAVE_OUTPUT else None

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

    # Intermediary step: printing/plotting results
    print(j, world.record_keeper.avg_dist)

    if j in plot_steps:
        plot_id = list(plot_steps).index(j) + 1
        plot_name = plot_path + f'{ACO_MODE}_no{plot_id}_iter{str(j).zfill(2)}'
        world.record_keeper.plot_best_paths(save_plot=SAVE_OUTPUT, path=plot_name)

    # Step 4: Resetting ants in world
    world.reset_ants()

# Step 5: Plot average distance travelled over iterations
plot_name = plot_path + f'{ACO_MODE}_avg_error_hist'
world.record_keeper.plot_error_hist(save_plot=SAVE_OUTPUT, path=plot_name)
