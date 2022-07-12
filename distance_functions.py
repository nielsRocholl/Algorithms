import numpy as np

"""
Returns the manhattan distance between two vectors
"""


def get_manhattan_distance(x, y):
    distances = [np.abs(x - y) for x, y in zip(x, y)]
    manhattan_distance = np.sum(distances) / len(distances)
    return manhattan_distance
