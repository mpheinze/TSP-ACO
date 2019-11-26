#! /usr/bin/python3

import os
import numpy as np

# calculating euclidian distance between two points
def euclidian_distance(p, q):    
    return np.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)

def get_output_path():
    '''
    Returning relevant path to place output files. Creating a new dir called aco_output
    '''
    output_path = os.getcwd() + '/aco_output'
    
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    prev_output_dirs = os.listdir(output_path)
    output_index = 1 if not prev_output_dirs else \
        max([int(_dir.split('_')[1].lstrip('0')) for _dir in prev_output_dirs]) + 1 
    
    new_path = output_path + f'/aco_{str(output_index).zfill(3)}/'
    os.mkdir(new_path)

    return new_path
