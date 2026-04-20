import math
def alpha_beta(node, depth, alpha, beta, is_maximizing, tree):
    if isinstance(tree[node], int):
        return tree[node]
    children = tree[node]
    if is_maximizing:
        max_eval = -math.inf
        for child in children:
            result = alpha_beta(child, depth + 1, alpha, beta, False, tree)
            max_eval = max(max_eval, result)
            alpha = max(alpha, result)
            if beta <= alpha:
                print(f"  Pruned at node {child}")
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in children:
            result = alpha_beta(child, depth + 1, alpha, beta, True, tree)
            min_eval = min(min_eval, result)
            beta = min(beta, result)
            if beta <= alpha:
                print(f"  Pruned at node {child}")
                break
        return min_eval
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': 3, 'I': 5, 'J': 2, 'K': 9,
    'L': 1, 'M': 7, 'N': 4, 'O': 6
}
result = alpha_beta('A', 0, -math.inf, math.inf, True, tree)
print(f"\nOptimal value: {result}")