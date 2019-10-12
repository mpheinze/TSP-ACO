import random
import numpy as np
import pandas as pd

from utils import distance_matrix
from matplotlib import pyplot as plt

# number of nodes on the map
N_NODES = 10


# generating random arrays of integers
x = [random.randint(1, 20) for i in range(N_NODES)]
y = [random.randint(1, 20) for i in range(N_NODES)]

node_list = list(zip(x, y))
dist_matrix = distance_matrix(node_list)


# scatter plotting nodes
fig, ax = plt.subplots(figsize=(6, 6))
plt.scatter(x, y, s=200, color='firebrick')
plt.show()