import numpy as np
from matplotlib import pyplot as plt

"""
Returns the manhattan distance between two vectors
"""


def get_manhattan_distance(x, y):
    distances = [np.abs(x - y) for x, y in zip(x, y)]
    manhattan_distance = np.sum(distances) / len(distances)
    return manhattan_distance


for i in range(100):
    x_1 = np.random.normal(5, 2)
    y_1 = np.random.normal(5, 2)
    x_2 = np.random.normal(15, 2)
    y_2 = np.random.normal(15, 2)
    plt.scatter(x_1, y_1, c='b')
    plt.scatter(x_2, y_2, c='b')

plt.savefig('cluster.jpeg')
