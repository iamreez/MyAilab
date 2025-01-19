def calculate_heuristic(blocks, goal):
    """
    Calculate the heuristic value for the Blocks World problem.

    Parameters:
    blocks (dict): A dictionary representing the current state, where each key is a block,
                   and the value is the block it is directly supported by (or None if it's on the table).
    goal (dict): A dictionary representing the goal state in the same format as blocks.

    Returns:
    int: The heuristic value for the current state.
    """
    heuristic = 0

    # Iterate through all blocks to compute their contribution to the heuristic
    for block, support in blocks.items():
        # Check if the current block's support matches the goal state
        if support == goal.get(block):
            # Correct support structure: Add +1 for every block in the support chain
            current = block
            while current:
                heuristic += 1
                current = blocks.get(current)
        else:
            # Incorrect support structure: Subtract -1 for every block in the support chain
            current = block
            while current:
                heuristic -= 1
                current = blocks.get(current)

    return heuristic


# Example usage
if __name__ == "__main__":
    # Define the current state
    current_state = {
        'A': 'B',  # A is on B
        'B': 'C',  # B is on C
        'C': None, # C is on the table
        'D': 'E',  # D is on E
        'E': None  # E is on the table
    }

    # Define the goal state
    goal_state = {
        'A': 'B',  # A is on B
        'B': 'C',  # B is on C
        'C': None, # C is on the table
        'D': None, # D is on the table
        'E': None  # E is on the table
    }

    heuristic_value = calculate_heuristic(current_state, goal_state)
    print(f"Heuristic value: {heuristic_value}")
