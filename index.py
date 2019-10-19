import numpy as np

import ant
import world
# import ant
# import world
# from ant import Ant
# from world import World

# number of nodes on the map
N_NODES = 10
N_ANTS = 100
RHO = 0.1
GAMMA = 1

world = world.World(N_NODES, N_ANTS, 20, RHO, GAMMA)
world.populate_world()

for j in range(100):
    for i in range(N_NODES-1):
        world.move_ants()

    print(world.avg_distance_travelled())

