print("number of queens is-------->>>:")
N = int(input())

# Initialize chessboard
# NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    # Checking for column j
    for k in range(0, i):
        if board[k][j] == 1:
            return True

    # Checking upper right diagonal
    k = i - 1
    l = j + 1
    while k >= 0 and l <= N - 1:
        if board[k][l] == 1:
            return True
        k -= 1
        l += 1

    # Checking upper left diagonal
    k = i - 1
    l = j - 1
    while k >= 0 and l >= 0:
        if board[k][l] == 1:
            return True
        k -= 1
        l -= 1

    return False

def n_queen(row):
    if row == N:
        # If all queens are placed successfully
        # Append the current board configuration to the solutions list
        all_possible_solutions.append([row[:] for row in board])
        return

    for j in range(0, N):
        if not is_attack(row, j):
            board[row][j] = 1

            # Place the next queen
            n_queen(row + 1)

            # Backtrack
            board[row][j] = 0

# List to store all possible solutions
all_possible_solutions = []

# Find all solutions
n_queen(0)

# Printing all solutions
for solution in all_possible_solutions:
    for row in solution:
        print(row)
    print()

# Print the total number of solutions
print("The Total solutions is:", len(all_possible_solutions))
