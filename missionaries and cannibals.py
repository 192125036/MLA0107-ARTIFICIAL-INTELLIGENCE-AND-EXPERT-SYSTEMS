from collections import deque

# Function to check if a state is valid
def is_valid(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right = state

    # Check if missionaries are outnumbered by cannibals
    if (missionaries_left > 0 and missionaries_left < cannibals_left) or \
       (missionaries_right > 0 and missionaries_right < cannibals_right):
        return False

    return True

# Function to generate valid next states
def next_states(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    valid_moves = []
    boat = 'left' if state[0] > 0 else 'right'

    for m, c in moves:
        if boat == 'left':
            new_state = (
                state[0] - m,
                state[1] - c,
                state[2] + m,
                state[3] + c
            )
        else:
            new_state = (
                state[0] + m,
                state[1] + c,
                state[2] - m,
                state[3] - c
            )

        if is_valid(new_state):
            valid_moves.append(new_state)

    return valid_moves

# Breadth-first search
def bfs():
    start_state = (3, 3, 0, 0)
    goal_state = (0, 0, 3, 3)

    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        visited.add(current_state)

        for next_state in next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None

# Solve the problem
solution = bfs()

# Print the solution
if solution:
    print("Solution found! Steps to move missionaries and cannibals across the river:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}: {state}")
else:
    print("No solution found.")
