from collections import deque

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def to_tuple(state):                               # FIX 1: helper to hash state
    return tuple(tuple(row) for row in state)

def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print("-----")

def bfs(start):
    queue = deque()
    visited = set()                                # FIX 2: set instead of list

    visited.add(to_tuple(start))                  # FIX 3: mark visited before enqueue
    queue.append((start, [start]))

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for step in path:
                print_state(step)
            print(f"Solved in {len(path)-1} moves.")
            return

        for neighbor in get_neighbors(state):
            if to_tuple(neighbor) not in visited:  # FIX 4: check before appending
                visited.add(to_tuple(neighbor))
                queue.append((neighbor, path + [neighbor]))

    print("No solution found.")

start = [[1, 3, 0],
         [6, 8, 4],
         [7, 5, 2]]

bfs(start)