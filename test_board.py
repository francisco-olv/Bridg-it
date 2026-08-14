from board import (
    EMPTY_SYMBOL,
    PLAYER1_SYMBOL,
    PLAYER2_SYMBOL,
    create_board,
    is_valid_board_size,
)


def test_is_valid_board_size():
    """Tests board size validation logic."""
    assert is_valid_board_size(5) is True
    assert is_valid_board_size(7) is True

    assert is_valid_board_size(4) is False
    assert is_valid_board_size(3) is False


def test_create_board_structure():
    """Tests if the board dimension is strictly N x N."""
    size = 5
    board = create_board(size)

    assert len(board) == size
    for row in board:
        assert len(row) == size


def test_create_board_initial_positions():
    """Tests initial placement of emojis in a 5x5 board."""
    board = create_board(5)

    # Check Player 1 starting symbol at (Row 0, Col 1)
    assert board[0][1] == PLAYER1_SYMBOL

    # Check Player 2 starting symbol at (Row 1, Col 0)
    assert board[1][0] == PLAYER2_SYMBOL

    # Check Empty cell at (Row 0, Col 0)
    assert board[0][0] == EMPTY_SYMBOL