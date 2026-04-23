# KNN Algorithm

import math

# Number of data points
n = int(input("Enter number of training points: "))

data = []

# Taking training data
for i in range(n):
    point = list(map(float, input(f"Enter point {i+1} (space separated): ").split()))
    label = input(f"Enter label for point {i+1}: ")
    data.append((point, label))

# Test point
test = list(map(float, input("Enter test point (space separated): ").split()))

# Value of k
k = int(input("Enter value of k: "))

# Distance function
def distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(len(p1))))

# Calculate distances
distances = []
for point, label in data:
    d = distance(point, test)
    distances.append((d, label))

# Sort distances
distances.sort()

# Get k nearest neighbors
neighbors = distances[:k]

# Count labels
count = {}
for _, label in neighbors:
    count[label] = count.get(label, 0) + 1

# Prediction
result = max(count, key=count.get)

print("Predicted class:", result)





# Enter number of training points: 5
# Enter point 1: 1 2
# Enter label for point 1: A
# Enter point 2: 2 3
# Enter label for point 2: A
# Enter point 3: 3 3
# Enter label for point 3: B
# Enter point 4: 6 5
# Enter label for point 4: B
# Enter point 5: 7 7
# Enter label for point 5: B
# Enter test point: 3 2
# Enter value of k: 3


# Expected Output
# Predicted class: A