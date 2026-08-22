"""Game logic module for managing moves, turns, and board states in Bridg-It."""

from board import EMPTY_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL
from validator import check_player1_victory, check_player2_victory


def is_valid_move(board: list[list[str]], row: int, col: int) -> bool:
    """Checks whether a proposed move is within boundaries and on an empty cell.

    Args:
        board (list[list[str]]): The current game board matrix.
        row (int): The target row index.
        col (int): The target column index.

    Returns:
        bool: True if the coordinates are valid and cell is empty, False otherwise.
    """
    size = len(board)

    # Validates if coordinates are inside matrix bounds [0, size - 1]
    if 0 <= row < size and 0 <= col < size:
        return board[row][col] == EMPTY_SYMBOL

    return False


def switch_player(current_player: str) -> str:
    """Switches the turn to the opposing player.

    Args:
        current_player (str): Symbol representing the player who just moved.

    Returns:
        str: Symbol of the next player to move.
    """
    if current_player == PLAYER1_SYMBOL:
        return PLAYER2_SYMBOL

    return PLAYER1_SYMBOL


def make_move(
    board: list[list[str]], row: int, col: int, current_player: str
) -> tuple[bool, str, bool]:
    """Executes a move on the board, updates turn, and evaluates victory status.

    Args:
        board (list[list[str]]): The current game board matrix.
        row (int): Target row index for the new piece.
        col (int): Target column index for the new piece.
        current_player (str): Symbol of the player attempting the move.

    Returns:
        tuple[bool, str, bool]: A tuple containing:
            - move_successful (bool): True if move was applied, False if invalid.
            - next_player (str): Symbol of the player for the subsequent turn.
            - winner_found (bool): True if this move completed a winning path.
    """
    # 1. Guard clause: abort immediately if move is illegal
    if not is_valid_move(board, row, col):
        return False, current_player, False

    # 2. Apply player symbol to the chosen empty cell
    board[row][col] = current_player

    # 3. Check if current player completed a winning path (passing board matrix)
    if current_player == PLAYER1_SYMBOL:
        winner_found = check_player1_victory(board)
    else:
        winner_found = check_player2_victory(board)

    # 4. Advance turn only if no victory was declared
    if winner_found:
        next_player = current_player
    else:
        next_player = switch_player(current_player)

    return True, next_player, winner_found