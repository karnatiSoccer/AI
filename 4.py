# K-means Clustering 

import numpy as np
import math

n = int(input("Enter number of data points: "))

data = []
for i in range(n):
    point = list(map(float, input(f"Enter point {i+1} (space separated): ").split()))
    data.append(point)

data = np.array(data)

k = int(input("Enter number of clusters (k): "))

centroids = data[:k]

# Distance function (Euclidean)
def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# K-means algorithm
for iteration in range(5):  # fixed iterations (easy for exam)
    clusters = [[] for _ in range(k)]

    # Step 2: Assign points to nearest centroid
    for point in data:
        distances = [distance(point, c) for c in centroids]
        min_index = distances.index(min(distances))
        clusters[min_index].append(point)

    # Step 3: Update centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            mean = tuple(sum(x)/len(x) for x in zip(*cluster))
            new_centroids.append(mean)
        else:
            new_centroids.append((0, 0))

    centroids = new_centroids

print("\nFinal Clusters:", clusters)
print("Final Centroids:", centroids)



# Enter number of data points: 6
# Enter point 1 (space separated): 1 2
# Enter point 2 (space separated): 1 4
# Enter point 3 (space separated): 2 3
# Enter point 4 (space separated): 8 7
# Enter point 5 (space separated): 9 8
# Enter point 6 (space separated): 8 9
# Enter number of clusters (k): 2


# ✅ Expected Output (approx)
# Clusters: [0, 0, 0, 1, 1, 1]

# Centroids:
#  [[1.33 3.  ]
#   [8.33 8.  ]]