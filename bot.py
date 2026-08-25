import random
from board import EMPTY_SYMBOL

def get_empty_positions(board: list[list[str]]) -> list[tuple[int, int]]:
    """
    Returns a list of empty positions on the board.
    
    Args:
        board (list): A 2D list representing the game board.
        
    Returns:
        list: A list of tuples representing the coordinates of empty positions.
    """
    size = len(board)
    return [
        (row, col)
        for row in range(size)
        for col in range(size)
        if board[row][col] == EMPTY_SYMBOL
    ]


def get_bot_move(board: list[list[str]]) -> tuple[int, int] | None:
    """
    Selects a random valid move from the available empty positions on the board.
    
    Args:
        board (list): A 2D list representing the game board.
        
    Returns:
        tuple | None: Coordinates (row, col) for the bot's move, or None if the board is full.
    """
    empty_positions = get_empty_positions(board)
    if not empty_positions:
        return None
    return random.choice(empty_positions)