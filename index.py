import numpy as np
from matplotlib import pyplot as plt
import ant
import world
from record_keeper import RecordKeeper


# number of nodes on the map
N_NODES = 10
N_ANTS = 500
N_ITERATIONS = 500

ALPHA = 1
BETA = 1
GAMMA = 1
RHO = 0.2

indx_list = []
dist_list = []

# initializing world
world = world.World(N_NODES, N_ANTS, 20, alpha=ALPHA, beta=BETA, gamma=GAMMA, rho=RHO)
world.populate_world()

for j in range(N_ITERATIONS):
    for i in range(N_NODES - 1):
        world.move_ants()

    world.update_phro()
    avg_dist = world.finalize_run()
    print(j, avg_dist)

    world.reset_ants()