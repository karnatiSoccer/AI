from collections import deque

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == goal_state

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            # Copy state
            new_state = [row[:] for row in state]

            # Swap zero with neighbor
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors

def bfs(start):
    queue = deque([(start, 0)])  # (state, depth)
    visited = []

    while queue:
        state, depth = queue.popleft()

        if is_goal(state):
            print("Goal reached in steps:", depth)
            return

        if state not in visited:
            visited.append(state)

            for neighbor in get_neighbors(state):
                queue.append((neighbor, depth + 1))

    print("No solution found")


# Example start state
start_state = [[1, 3, 0],
         [6, 8, 4],
         [7, 5, 2]]


        

bfs(start_state)