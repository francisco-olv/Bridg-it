from board import create_board, PLAYER1_SYMBOL, PLAYER2_SYMBOL
from validator import check_player1_victory, check_player2_victory


def test_no_victory_on_initial_board():
    """Tests that a fresh board has no winner for either player."""
    board = create_board(5)

    assert check_player1_victory(board) is False
    assert check_player2_victory(board) is False


def test_player1_victory_connected_path():
    """Tests that Player 1 wins when a continuous top-to-bottom path exists."""
    board = create_board(5)

    # Connecting Player 1 pieces vertically on Column 1
    board[1][1] = PLAYER1_SYMBOL
    board[3][1] = PLAYER1_SYMBOL

    assert check_player1_victory(board) is True
    assert check_player2_victory(board) is False


def test_player2_victory_connected_path():
    """Tests that Player 2 wins when a continuous left-to-right path exists."""
    board = create_board(5)

    # Connecting Player 2 pieces horizontally on Row 1
    board[1][1] = PLAYER2_SYMBOL
    board[1][3] = PLAYER2_SYMBOL

    assert check_player1_victory(board) is False
    assert check_player2_victory(board) is True


def test_player1_disconnected_pieces_no_victory():
    """Tests that isolated pieces on top and bottom do not trigger a victory."""
    board = create_board(5)

    # Placed a piece near the bottom, but left (2, 1) empty so there is no continuous path
    board[3][1] = PLAYER1_SYMBOL

    assert check_player1_victory(board) is False

def test_player2_disconnected_pieces_no_victory():
    """Tests that isolated pieces on left and right do not trigger a victory."""
    board = create_board(5)

    # Placed a piece near the right, but left (1, 2) empty so there is no continuous path
    board[1][3] = PLAYER2_SYMBOL

    assert check_player2_victory(board) is False