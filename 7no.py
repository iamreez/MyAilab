import heapq
import copy

def is_solvable(puzzle):
    """Check if the 8-puzzle is solvable."""
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = sum(
        1 for i in range(len(flat_puzzle)) for j in range(i + 1, len(flat_puzzle)) if flat_puzzle[i] > flat_puzzle[j]
    )
    return inversions % 2 == 0

def heuristic(state, goal):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), len(state))
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    """Generate neighbors by moving the blank space (0) in the puzzle."""
    neighbors = []
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state) and 0 <= ny < len(state[0]):
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def a_star(start, goal):
    """Solve the 8-puzzle problem using A* algorithm."""
    if not is_solvable(start):
        return "The puzzle is unsolvable."

    goal_flat = [num for row in goal for num in row]

    open_list = []
    heapq.heappush(open_list, (0, start, []))
    closed_set = set()

    while open_list:
        _, current, path = heapq.heappop(open_list)

        if current == goal:
            return path + [current]

        closed_set.add(tuple(tuple(row) for row in current))

        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)

            if neighbor_tuple not in closed_set:
                g = len(path) + 1
                h = heuristic(neighbor, goal_flat)
                f = g + h
                heapq.heappush(open_list, (f, neighbor, path + [current]))

    return "No solution found."

if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution = a_star(start_state, goal_state)

    if isinstance(solution, str):
        print(solution)
    else:
        print("Solution path:")
        for step in solution:
            for row in step:
                print(row)
            print()
