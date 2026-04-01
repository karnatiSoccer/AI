from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque()

    # (jug1, jug2, path)
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        new_path = path + [(x, y)]

        # Check goal
        if x == target or y == target:
            for state in new_path:
                print(state[0], state[1])
                print("-----")
            print(f"Solved in {len(new_path)-1} steps.")
            return

        # Possible operations
        next_states = [
            (cap1, y),        # Fill Jug1
            (x, cap2),        # Fill Jug2
            (0, y),           # Empty Jug1
            (x, 0),           # Empty Jug2
            # Pour Jug1 → Jug2
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            # Pour Jug2 → Jug1
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], new_path))

    print("No solution found")


# Example
water_jug_bfs(4, 3, 2)