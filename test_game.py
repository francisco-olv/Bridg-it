from board import EMPTY_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL
from game import is_valid_move, switch_player, make_move


def test_is_valid_move_within_bounds_and_empty_cell():
    """Tests that a move is valid when within bounds and on an empty cell."""
    board = [
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
    ]

    assert is_valid_move(board, 1, 1) is True


def test_is_valid_move_out_of_bounds():
    """Tests that a move is invalid when out of board bounds."""
    board = [
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
    ]

    assert is_valid_move(board, -1, 0) is False
    assert is_valid_move(board, 3, 0) is False
    assert is_valid_move(board, 0, -1) is False
    assert is_valid_move(board, 0, 3) is False 


def test_is_valid_move_on_occupied_cell():
    """Tests that a move is invalid when the target cell is already occupied."""
    board = [
        [EMPTY_SYMBOL, PLAYER1_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
    ]

    assert is_valid_move(board, 0, 1) is False 


def test_switch_player_functionality():
    """Tests that the switch_player function correctly alternates between players."""
    assert switch_player(PLAYER1_SYMBOL) == PLAYER2_SYMBOL
    assert switch_player(PLAYER2_SYMBOL) == PLAYER1_SYMBOL


def test_make_move_invalid_does_not_modify_state():
    """Tests that an invalid move fails, preserves current player, and finds no winner."""
    board = [
        [EMPTY_SYMBOL, PLAYER1_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
    ]

    move_successful, next_player, winner_found = make_move(
        board, 0, -1, PLAYER1_SYMBOL
    )

    assert move_successful is False
    assert next_player == PLAYER1_SYMBOL
    assert winner_found is False


def test_make_move_valid_without_victory():
    """Tests that a valid non-winning move updates the board, switches player, and returns success."""
    board = [
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
    ]

    move_successful, next_player, winner_found = make_move(
        board, 0, 0, PLAYER1_SYMBOL
    )

    assert move_successful is True
    assert next_player == PLAYER2_SYMBOL
    assert winner_found is False
    assert board[0][0] == PLAYER1_SYMBOL  


def test_make_move_valid_and_winner_found():
    """Tests that a winning move updates the board, keeps current player, and declares victory."""
    board = [
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
    ]

    move_successful, next_player, winner_found = make_move(
        board, 2, 0, PLAYER1_SYMBOL
    )

    assert move_successful is True
    assert next_player == PLAYER1_SYMBOL
    assert winner_found is True
    assert board[2][0] == PLAYER1_SYMBOL

