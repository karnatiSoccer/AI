def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    turn = 0

    while (turn < 9):
        print_board(board)

        print(f"Player {current_player}, enter row and column (0-2): ")
        row = int(input("Row: "))
        col = int(input("Column: "))

        # Check if cell is empty
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

        turn += 1

    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()