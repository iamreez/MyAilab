import copy

def heuristic(state, goal):
    """
    Calculate the Manhattan distance heuristic.
    
    Parameters:
    state (list): Current puzzle state as a 2D list.
    goal (list): Goal puzzle state as a 2D list.

    Returns:
    int: Total Manhattan distance.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Ignore the blank tile
                goal_i, goal_j = [(row, col) for row in range(3) for col in range(3) if goal[row][col] == state[i][j]][0]
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

def get_neighbors(state):
    """
    Generate all possible moves (neighbors) for the given state.

    Parameters:
    state (list): Current puzzle state as a 2D list.

    Returns:
    list: List of neighbor states.
    """
    neighbors = []
    # Locate the blank tile (0)
    x, y = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]

    # Define possible moves
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def steepest_ascent(initial_state, goal_state):
    """
    Solve the 8-puzzle using the steepest ascent hill climbing algorithm.

    Parameters:
    initial_state (list): Starting puzzle state as a 2D list.
    goal_state (list): Goal puzzle state as a 2D list.

    Returns:
    list: Sequence of states from initial to goal (or the best attempt).
    """
    current_state = initial_state
    path = [current_state]

    while True:
        current_heuristic = heuristic(current_state, goal_state)
        neighbors = get_neighbors(current_state)

        # Evaluate all neighbors and pick the best one
        best_neighbor = None
        best_heuristic = float("inf")
        for neighbor in neighbors:
            h = heuristic(neighbor, goal_state)
            if h < best_heuristic:
                best_neighbor = neighbor
                best_heuristic = h

       
        if best_heuristic >= current_heuristic:
            break

      
        current_state = best_neighbor
        path.append(current_state)

    return path

# Example usage
if __name__ == "__main__":
    initial = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution_path = steepest_ascent(initial, goal)

    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
