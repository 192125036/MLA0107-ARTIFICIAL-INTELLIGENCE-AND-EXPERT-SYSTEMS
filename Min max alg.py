import math

# Define the game board and players
X = 'X'
O = 'O'
EMPTY = None

# Function to evaluate the game state
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return 10
            elif board[i][0] == O:
                return -10
        
        # Columns
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == X:
                return 10
            elif board[0][i] == O:
                return -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return 10
        elif board[0][0] == O:
            return -10
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return 10
        elif board[0][2] == O:
            return -10
    
    # If no winner, return 0 (tie)
    return 0

# Function to check if the game is over
def game_over(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False  # Empty cell, game is not over yet
    return True  # All cells filled, game over

# Function to find the best move using Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Base cases: return score if game is over or depth limit reached
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if game_over(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = EMPTY
        return best

# Function to find the optimal move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = X
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Function to print the game board
def print_board(board):
    for row in board:
        print(row)

# Main function to play the game
def play_game():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    print("Let's play Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        player_move = input("Enter your move (row column): ")
        row, col = map(int, player_move.split())

        if board[row][col] == EMPTY:
            board[row][col] = O
        else:
            print("Invalid move. Try again.")
            continue

        if game_over(board):
            break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = X

        print("\nYour move:")
        print_board(board)

    print("\nGame Over!")
    print_board(board)
    score = evaluate(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a tie!")

# Start the game
play_game()
