import random
import numpy as np
from distance_functions import get_manhattan_distance
from data import kmeans_data


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


def get_k_means(user_feature_map: dict, k: int):
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


centroids = get_k_means(user_feature_map=kmeans_data, k=2)

for cnt, centroid in enumerate(centroids):
    print(f'Centroid {cnt}: {centroid}')

dataset = {'t_0': [-1.479, -1.895, -2.046, -1.710],
           't_1': [-2.478, -1.950, -2.046, -1.710],

           't_100': [-1.232, -1.844, -1.849, -2.472],
           }
