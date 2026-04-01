import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue (min-heap)
    queue = []
    heapq.heappush(queue, (0, start))  # (cost, node)

    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        # If goal is reached
        if node == goal:
            print("Minimum cost to reach goal:", cost)
            return

        if node not in visited:
            visited.add(node)

            # Explore neighbors
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))

    print("Goal not reachable")


# Example graph (Adjacency list)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 6)],
    'C': [('F', 4)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Function call
uniform_cost_search(graph, 'A', 'G')