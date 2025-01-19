def calculate_heuristic_tictactoe(board, player, opponent):
    """
    Calculate the heuristic value for a given Tic-Tac-Toe board state.

    Parameters:
    board (list of list): A 3x3 list representing the Tic-Tac-Toe board.
                          'X' for player X, 'O' for player O, and None for empty cells.
    player (str): The symbol representing the current player ('X' or 'O').
    opponent (str): The symbol representing the opponent ('X' or 'O').

    Returns:
    int: The heuristic value of the board.
    """
    def is_open_line(line, symbol):
        """
        Check if a line (row, column, or diagonal) is open for the given symbol.
        A line is open if it has no opponent symbols.
        """
        return all(cell in (symbol, None) for cell in line)

    heuristic = 0

    # Check rows, columns, and diagonals
    for i in range(3):
        row = board[i]
        col = [board[j][i] for j in range(3)]

        # Add to heuristic if the row/column is open for the player or opponent
        if is_open_line(row, player):
            heuristic += 1
        if is_open_line(row, opponent):
            heuristic -= 1

        if is_open_line(col, player):
            heuristic += 1
        if is_open_line(col, opponent):
            heuristic -= 1

    # Check diagonals
    main_diag = [board[i][i] for i in range(3)]
    anti_diag = [board[i][2 - i] for i in range(3)]

    if is_open_line(main_diag, player):
        heuristic += 1
    if is_open_line(main_diag, opponent):
        heuristic -= 1

    if is_open_line(anti_diag, player):
        heuristic += 1
    if is_open_line(anti_diag, opponent):
        heuristic -= 1

    return heuristic

# Example usage:
if __name__ == "__main__":
    # Define the Tic-Tac-Toe board
    board = [
        ['X', 'O', None],
        ['X', None, 'O'],
        [None, None, 'X']
    ]

    # Define the player and opponent symbols
    player = 'X'
    opponent = 'O'

    heuristic_value = calculate_heuristic_tictactoe(board, player, opponent)
    print(f"Heuristic value: {heuristic_value}")
