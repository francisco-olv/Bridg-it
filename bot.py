import random
import copy
from board import EMPTY_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL
from validator import check_player1_victory, check_player2_victory

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


def check_victory(board: list[list[str]], player_symbol: str) -> bool:
    """Helper function to route victory validation based on player symbol."""
    if player_symbol == PLAYER1_SYMBOL:
        return check_player1_victory(board)
    elif player_symbol == PLAYER2_SYMBOL:
        return check_player2_victory(board)
    return False


def find_winning_move(board: list[list[str]], player_symbol: str) -> tuple[int, int] | None:
    """
    Simulates moves for a given player to find an immediate winning move.
    
    Args:
        board (list): The current game board.
        player_symbol (str): Symbol of the player to check for a winning move.
        
    Returns:
        tuple | None: The coordinates (row, col) that lead to a win, or None if none exist.
    """
    safety_board = copy.deepcopy(board)
    
    for row, col in get_empty_positions(board):
        safety_board[row][col] = player_symbol
        is_win = check_victory(safety_board, player_symbol)
        safety_board[row][col] = EMPTY_SYMBOL 
        
        if is_win:
            return (row, col)
            
    return None


def get_bot_move(
    board: list[list[str]], 
    bot_symbol: str, 
    human_symbol: str
) -> tuple[int, int] | None:
    """
    Selects the best available move for the bot following priority:
    1. Winning move (Offensive)
    2. Blocking move (Defensive)
    3. Random valid move
    """
    winning_move = find_winning_move(board, bot_symbol)
    if winning_move:
        return winning_move
        
    blocking_move = find_winning_move(board, human_symbol)
    if blocking_move:
        return blocking_move
        
    empty_positions = get_empty_positions(board)
    if not empty_positions:
        return None
        
    return random.choice(empty_positions)