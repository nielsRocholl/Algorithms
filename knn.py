import numpy as np
from data import knn_data

"""
Predict label of feature based on k nearest neighbors
"""


def predict_label(training_set, unlabelled_features, k, label_key="passed"):
    labels = []
    # find k nearest neighbors
    knn = find_k_nearest_neighbors(training_set, unlabelled_features, k)
    # find labels of the k nearest neighbors
    for key in knn:
        labels.append(training_set[key][label_key])
    # determine the most prominent label
    label = max(set(labels), key=labels.count)
    return label


"""
Find k nearest neighbors based on euclidean distance
"""


def find_k_nearest_neighbors(training_set, unlabelled_features, k):
    # list holds euclidean distances between given feature and other examples
    euclid_dist = []
    for student in training_set:
        training_features = training_set[student]['features']
        distance = np.linalg.norm(np.array(unlabelled_features) - np.array(training_features))
        euclid_dist.append([distance, student])
    # sort list in ascending order
    euclid_dist_sorted = sorted(euclid_dist, key=lambda x: x[0])
    # return k nearest neighbors
    nearest_neighbors = [x[1] for x in euclid_dist_sorted][0:k]
    return nearest_neighbors


# study time dataset
study_time_dataset = {
    "student 0": {"passed": False, "features": [7.847, 5.391]},
    "student 1": {"passed": False, "features": [1.641, 4.687]},
    "student 2": {"passed": False, "features": [2.871, 8.806]},
    "student 3": {"passed": False, "features": [6.473, 15.439]},
    "student 4": {"passed": False, "features": [16.037, 0.2788]},
    "student 5": {"passed": True, "features": [13.127, 15.713]},
    "student 6": {"passed": True, "features": [18.787, 25.425]},
    "student 7": {"passed": True, "features": [5.161, 25.306]},
    "student 8": {"passed": True, "features": [13.168, 11.499]},
    "student 9": {"passed": True, "features": [19.271, 15.395]}
}

# example input 16 hours exercises and 17 hours reading
unlabelled_features = [16, 17]
# predict the label of 'unlabelled_features'
label = predict_label(training_set=study_time_dataset, unlabelled_features=[16, 17], k=3, label_key='passed')
# label = true if passed, label = false if failed
print(f'Label predicted by KNN: {label} ')
