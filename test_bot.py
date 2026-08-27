from bot import get_empty_positions, check_victory, find_winning_move, get_bot_move
from board import EMPTY_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL

def test_get_empty_positions():
    board = [
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, PLAYER2_SYMBOL],
        [EMPTY_SYMBOL, PLAYER1_SYMBOL, EMPTY_SYMBOL],
        [PLAYER2_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL]
    ]
    expected_empty_positions = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 2)]
    assert get_empty_positions(board) == expected_empty_positions


def test_check_victory():
    board_player1_win = [
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL]
    ]
    assert check_victory(board_player1_win, PLAYER1_SYMBOL) is True

    board_player2_win = [
        [PLAYER2_SYMBOL, PLAYER2_SYMBOL, PLAYER2_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL]
    ]
    assert check_victory(board_player2_win, PLAYER2_SYMBOL) is True

    board_no_win = [
        [PLAYER1_SYMBOL, PLAYER2_SYMBOL, PLAYER1_SYMBOL],
        [PLAYER2_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL],
        [PLAYER2_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL]
    ]
    assert check_victory(board_no_win, PLAYER1_SYMBOL) is False
    assert check_victory(board_no_win, PLAYER2_SYMBOL) is False


def test_find_winning_move():
    board = [
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [PLAYER1_SYMBOL, PLAYER1_SYMBOL, EMPTY_SYMBOL],
        [PLAYER2_SYMBOL, EMPTY_SYMBOL, PLAYER2_SYMBOL]
    ]
    # Player 1 can win by placing at (2, 1)
    assert find_winning_move(board, PLAYER1_SYMBOL) == (2, 1)

    # Player 2 can win by placing at (2, 1)
    assert find_winning_move(board, PLAYER2_SYMBOL) == (2, 1)

    # No winning move available
    board_full = [
        [PLAYER1_SYMBOL, PLAYER2_SYMBOL, PLAYER1_SYMBOL],
        [PLAYER2_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL],
        [PLAYER2_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL]
    ]
    assert find_winning_move(board_full, PLAYER1_SYMBOL) is None
    assert find_winning_move(board_full, PLAYER2_SYMBOL) is None


def test_get_bot_move():
    board = [
        [PLAYER1_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
        [PLAYER1_SYMBOL, PLAYER1_SYMBOL, EMPTY_SYMBOL],
        [PLAYER2_SYMBOL, EMPTY_SYMBOL, PLAYER2_SYMBOL]
    ]
    # Bot (Player 1) should take the winning move at (2, 1)
    assert get_bot_move(board, PLAYER1_SYMBOL, PLAYER2_SYMBOL) == (2, 1)

    # Bot (Player 2) should block Player 1's winning move at (2, 1)
    assert get_bot_move(board, PLAYER2_SYMBOL, PLAYER1_SYMBOL) == (2, 1)

    # If no winning or blocking moves are available, return a random valid move
    board_no_win_block = [
        [PLAYER1_SYMBOL, PLAYER2_SYMBOL, PLAYER1_SYMBOL],
        [PLAYER2_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL],
        [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL]
    ]
    bot_move = get_bot_move(board_no_win_block, PLAYER1_SYMBOL, PLAYER2_SYMBOL)
    assert bot_move in [(2, 0), (2, 1), (2, 2)]