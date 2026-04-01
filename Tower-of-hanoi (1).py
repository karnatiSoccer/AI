def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1

    moves = 0

    # Move n-1 disks from source → auxiliary
    moves += tower_of_hanoi(n-1, source, destination, auxiliary)

    # Move nth disk
    print(f"Move disk {n} from {source} to {destination}")
    moves += 1

    # Move n-1 disks from auxiliary → destination
    moves += tower_of_hanoi(n-1, auxiliary, source, destination)

    return moves


# Example
n = 3
total_moves = tower_of_hanoi(n, 'A', 'B', 'C')

print(f"Solved in {total_moves} moves.")





# def tower_of_hanoi(num, source, aux, target):
#     """
# 	num (int): Number of disks.
#     source (str): The name of the source tower.
#     aux (str): The name of the auxiliary tower.
#     target (str): The name of the target tower.
#     """
#     if num == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     # Move num-1 disks from source to auxiliary
#     tower_of_hanoi(num - 1, source, target, aux)
#     print(f"Move disk {num} from {source} to {target}")
#     # Move the num-1 disks from auxiliary to target
#     tower_of_hanoi(num - 1, aux, source, target)

# # Example usage
# num_disks = 3
# tower_of_hanoi(num_disks, "A", "B", "C")