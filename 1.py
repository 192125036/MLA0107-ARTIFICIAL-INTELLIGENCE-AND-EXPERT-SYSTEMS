from collections import deque

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]

# Function to find the possible moves from a given state
def possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is None:
                if i > 0:
                    moves.append((i - 1, j))  # Move empty space up
                if i < 2:
                    moves.append((i + 1, j))  # Move empty space down
                if j > 0:
                    moves.append((i, j - 1))  # Move empty space left
                if j < 2:
                    moves.append((i, j + 1))  # Move empty space right
                return moves

# Function to perform a move on the puzzle
def make_move(state, move):
    new_state = [row[:] for row in state]
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(3):
            if new_state[i][j] is None:
                empty_i, empty_j = i, j
                break

    new_i, new_j = move
    # Swap the empty space with the tile to be moved
    new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
    return new_state

# Function to perform a breadth-first search to solve the puzzle
def solve_puzzle(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        
        visited.add(tuple(map(tuple, state)))
        moves = possible_moves(state)
        
        for move in moves:
            new_state = make_move(state, move)
            if tuple(map(tuple, new_state)) not in visited:
                new_path = path + [move]
                queue.append((new_state, new_path))

    return None

# Example initial state (scrambled)
initial_state = [
    [2, 8, 3],
    [1, None, 4],
    [7, 6, 5]
]

solution = solve_puzzle(initial_state)
if solution:
    print("Solution Steps:")
    for step, move in enumerate(solution, 1):
        print(f"Step {step}: Move {move}")
else:
    print("No solution found.")
 
