from collections import deque
from board import PLAYER1_SYMBOL, PLAYER2_SYMBOL


def check_player1_victory(board: list[list[str]]) -> bool:
    """Checks if Player 1 (🔴) connected top to bottom using BFS.

    Args:
        board (list[list[str]]): The N x N game board matrix.

    Returns:
        bool: True if Player 1 formed a connected path from top to bottom.
    """
    size = len(board)

    # 1. Identify initial positions for Player 1 on Row 0 (Top)
    start_cells = [(0, col) for col in range(size) if board[0][col] == PLAYER1_SYMBOL]

    # If there are no pieces at the top, victory is impossible
    if not start_cells:
        return False

    # 2. Queue for Breadth-First Search (BFS) exploration
    queue = deque(start_cells)

    # 3. Visited matrix to prevent infinite loops
    visited = [[False] * size for _ in range(size)]
    for r, c in start_cells:
        visited[r][c] = True

    # 4. The 4 orthogonal movement directions: (row_delta, col_delta)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 5. BFS Main Loop
    while queue:
        row, col = queue.popleft()

        # VICTORY CONDITION: Reached the bottom row!
        if row == size - 1:
            return True

        # Explore the 4 neighboring cells (Up, Down, Left, Right)
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # Step A: Check if the target position is within matrix boundaries
            if 0 <= new_row < size and 0 <= new_col < size:
                # Step B: Check if it contains Player 1 symbol and hasn't been visited yet
                if board[new_row][new_col] == PLAYER1_SYMBOL and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

    return False


def check_player2_victory(board: list[list[str]]) -> bool:
    """Checks if Player 2 (🟡) connected left to right using BFS.

    Args:
        board (list[list[str]]): The N x N game board matrix.

    Returns:
        bool: True if Player 2 formed a connected path from left to right.
    """
    size = len(board)

    # 1. Identify initial positions for Player 2 on Column 0 (Left)
    start_cells = [(row, 0) for row in range(size) if board[row][0] == PLAYER2_SYMBOL]

    if not start_cells:
        return False

    queue = deque(start_cells)
    visited = [[False] * size for _ in range(size)]
    for r, c in start_cells:
        visited[r][c] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col = queue.popleft()

        # VICTORY CONDITION: Reached the rightmost column!
        if col == size - 1:
            return True

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < size and 0 <= new_col < size:
                if board[new_row][new_col] == PLAYER2_SYMBOL and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

    return False