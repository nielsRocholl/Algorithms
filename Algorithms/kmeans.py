import random
import numpy as np
from distance_functions import get_manhattan_distance


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


"""
Calculate the new centroids by taking the average of average fo each cluster. 
Also check if the new centroids are equal to the old ones and assign boolean value to 'changed'
"""


def calculate_new_centroids(clusters, old_centroids):
    centroids = []
    for cluster in clusters:
        centroids.append(list(np.mean(clusters[cluster], axis=0)))
    changed = old_centroids != centroids
    return centroids, changed


"""
K-means algorithm, returns a list containing the K means, indicating the centroids of k clusters.
Input should be a dict containing the features. Features can be a list of any any size (not a matrix). 
"""


def get_k_means(user_feature_map, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the initial users, to be used as centroids.
    initial_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)
    # Get the actual 4d points instead of dict
    centroids = [user_feature_map[centroid] for centroid in initial_centroid_users]
    # this variable tracks if the centroids change after being updated
    changed = True
    # keep count of iterations since we want to execute at least 10 iteration of k-means
    i = 0
    while changed and i < 10:
        clusters = {str(centroid): [] for centroid in centroids}
        # loop through all feature maps
        for feature_map in user_feature_map:
            # find the closest centroid for each feature map
            closest = [None, None]
            for centroid in centroids:
                distance = get_manhattan_distance(centroid, user_feature_map[feature_map])
                if closest[0] is None or distance < closest[1]:
                    closest = [centroid, distance]
            # get the cluster of the closest centroid
            cluster = clusters[str(closest[0])]
            # append the current feature map to that cluster
            cluster.append(user_feature_map[feature_map])
            # update the clusters dictionary accordingly
            clusters[str(closest[0])] = cluster
        centroids, changed = calculate_new_centroids(clusters, centroids)
        i += 1
    return centroids


# Example of the input data
data = {
    "uid_0": [-1.479359467505669, -1.895497044385029, -2.0461402601759096, -1.7109256402185178],
    "uid_1": [-1.8284426855307128, -1.714098142408679, -0.9893682669649455, -1.5766569391907947],
    "uid_2": [-1.8398933218386004, -1.7896757009107565, -1.1370177175666063, -1.0218512556903283],
    "uid_3": [-1.23224975874512, -1.8447858273094768, -1.8496517744301924, -2.4720755654344186],
    "uid_4": [-1.7714737791268318, -1.2725603446513774, -1.5512094954034525, -1.2589442628984848],
}

get_k_means(data, 2)
