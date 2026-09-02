# Board representation constants
PLAYER1_SYMBOL = "🔴"
PLAYER2_SYMBOL = "🔵"
EMPTY_SYMBOL = "🟩"


def create_board(size: int) -> list[list[str]]:
    """Creates an N x N matrix for the Bridg-It board game.

    Args:
        size (int): The dimension of the square board (N x N).

    Returns:
        list[list[str]]: A 2D list representing the board matrix filled with
            player starting symbols and empty cells.
    """
    board = []
    for row in range(size):
        new_row = []
        for col in range(size):
            if row % 2 == 0 and col % 2 != 0:
                new_row.append(PLAYER1_SYMBOL)
            elif row % 2 != 0 and col % 2 == 0:
                new_row.append(PLAYER2_SYMBOL)
            else:
                new_row.append(EMPTY_SYMBOL)
        board.append(new_row)
    return board


def is_valid_board_size(size: int) -> bool:
    """Validates if the provided board size meets the game rules.

    Args:
        size (int): The board size to validate.

    Returns:
        bool: True if size is an odd integer greater than or equal to 5,
            False otherwise.
    """
    return size >= 5 and size % 2 != 0


def display_board(board: list[list[str]]) -> None:
    """Prints the board matrix in the terminal.

    Args:
        board (list[list[str]]): The board matrix to be displayed.
    """
    size = len(board)
    print("\n   ", end="")
    for col in range(size):
        print(f" {col} ", end="")
    print()

    for row in range(size):
        print(f"{row:2d} ", end="")
        for col in range(size):
            print(f" {board[row][col]} ", end="")
        print()
    print()


# Direct execution block for terminal preview
if __name__ == "__main__":
    test_size = 5
    if is_valid_board_size(test_size):
        print(f"--- Bridg-It Board Preview ({test_size}x{test_size}) ---")
        my_board = create_board(test_size)
        display_board(my_board)