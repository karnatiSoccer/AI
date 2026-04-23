import numpy as np
# # Decision Trees
class DecisionTree:
    def __init__(self, max_depth=5): self.md = max_depth
    def fit(self, X, y): self.tree = self._build(X, y); return self
    def _build(self, X, y, d=0):
        if d == self.md or len(set(y)) == 1: return np.bincount(y).argmax()
        e = lambda y: -sum(p*np.log2(p) for p in np.bincount(y)/len(y) if p)
        best = max(((i, t, e(y) - sum(len(y[m])/len(y)*e(y[m]) for m in (X[:, i] <= t, X[:, i] > t)))
                    for i in range(X.shape[1]) for t in np.unique(X[:, i])), key=lambda x: x[2], default=(None, None, 0))
        if best[2] == 0: return np.bincount(y).argmax()
        m = X[:, best[0]] <= best[1]
        return (best[0], best[1], self._build(X[m], y[m], d+1), self._build(X[~m], y[~m], d+1))
    def _pred(self, x, n): return n if isinstance(n, (int, np.int64)) else self._pred(x, n[2] if x[n[0]] <= n[1] else n[3])
    def predict(self, X): return np.array([self._pred(x, self.tree) for x in X])



# # Enter number of data points: 5
# # Enter features for point 1 (space separated): 1 2
# # Enter label for point 1: A
# # Enter features for point 2 (space separated): 2 3
# # Enter label for point 2: A
# # Enter features for point 3 (space separated): 3 4
# # Enter label for point 3: B
# # Enter features for point 4 (space separated): 6 7
# # Enter label for point 4: B
# # Enter features for point 5 (space separated): 7 8
# # Enter label for point 5: B
# # Enter test data (space separated): 2 2


# # ✅ Expected Output
# # Prediction: A


# import math

# # Dataset
# data = [
#     ['Sunny', 'Hot', 'High', 'Weak', 'No'],
#     ['Sunny', 'Hot', 'High', 'Strong', 'No'],
#     ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
#     ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
#     ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
#     ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
#     ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
#     ['Sunny', 'Mild', 'High', 'Weak', 'No'],
#     ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
#     ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
# ]

# labels = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# # Entropy function
# def entropy(data):
#     total = len(data)
#     yes = sum(1 for row in data if row[-1] == 'Yes')
#     no = total - yes

#     if yes == 0 or no == 0:
#         return 0

#     p_yes = yes / total
#     p_no = no / total

#     return - (p_yes * math.log2(p_yes) + p_no * math.log2(p_no))


# # Split data
# def split_data(data, index, value):
#     return [row for row in data if row[index] == value]


# # Best attribute with IG printing
# def best_attribute(data, labels):
#     base_entropy = entropy(data)
#     print("\nCurrent Entropy:", round(base_entropy, 3))

#     best_gain = -1
#     best_index = -1

#     for i in range(len(labels)):
#         values = set(row[i] for row in data)
#         new_entropy = 0

#         for val in values:
#             subset = split_data(data, i, val)
#             prob = len(subset) / len(data)
#             new_entropy += prob * entropy(subset)

#         gain = base_entropy - new_entropy
#         print(f"IG({labels[i]}) = {round(gain, 3)}")

#         if gain > best_gain:
#             best_gain = gain
#             best_index = i

#     print("Best Attribute:", labels[best_index])
#     return best_index


# # Build tree
# def build_tree(data, labels):
#     results = [row[-1] for row in data]

#     # If all same class
#     if results.count(results[0]) == len(results):
#         return results[0]

#     if len(labels) == 0:
#         return max(set(results), key=results.count)

#     best_idx = best_attribute(data, labels)
#     best_label = labels[best_idx]

#     tree = {best_label: {}}

#     values = set(row[best_idx] for row in data)

#     for val in values:
#         subset = split_data(data, best_idx, val)

#         new_labels = labels[:best_idx] + labels[best_idx+1:]
#         new_subset = [row[:best_idx] + row[best_idx+1:] for row in subset]

#         print(f"\nSplitting {best_label} = {val}")

#         tree[best_label][val] = build_tree(new_subset, new_labels)

#     return tree


# # Prediction function
# def predict(tree, labels, test):
#     if not isinstance(tree, dict):
#         return tree

#     root = list(tree.keys())[0]
#     root_index = labels.index(root)

#     value = test[root_index]

#     subtree = tree[root].get(value)

#     if subtree is None:
#         return "Unknown"

#     # Remove used feature
#     new_labels = labels[:root_index] + labels[root_index+1:]
#     new_test = test[:root_index] + test[root_index+1:]

#     return predict(subtree, new_labels, new_test)


# # Build tree
# tree = build_tree(data, labels)
# print("\nFinal Tree:\n", tree)


# # Test prediction
# test_sample = ['Sunny', 'Cool', 'High', 'Strong']
# result = predict(tree, labels, test_sample)

# print("\nTest Sample:", test_sample)
# print("Prediction:", result)