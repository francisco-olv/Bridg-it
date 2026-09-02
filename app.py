import streamlit as st
from board import create_board, EMPTY_SYMBOL, PLAYER1_SYMBOL, PLAYER2_SYMBOL
from validator import check_player1_victory, check_player2_victory
from bot import get_bot_move, check_victory


def init_game_state():
    """Initializes or resets the game state variables in st.session_state."""
    if "board" not in st.session_state:
        st.session_state.board = create_board(size=5)
    if "current_player" not in st.session_state:
        st.session_state.current_player = PLAYER1_SYMBOL
    if "winner" not in st.session_state:
        st.session_state.winner = None
    if "scores" not in st.session_state:
        st.session_state.scores = {PLAYER1_SYMBOL: 0, PLAYER2_SYMBOL: 0}


def reset_game():
    """Resets the board and current turn while preserving active scores."""
    st.session_state.board = create_board(size=5)
    st.session_state.current_player = PLAYER1_SYMBOL
    st.session_state.winner = None


def reset_scores():
    """Resets the scoreboard back to zero and cleans active game state."""
    st.session_state.scores = {PLAYER1_SYMBOL: 0, PLAYER2_SYMBOL: 0}
    reset_game()  # Clears winner state to prevent repeated victory balloons


def on_game_mode_change():
    """Callback triggered when changing game mode to reset the active board state."""
    reset_game()


def handle_move(row: int, col: int):
    """Handles a move placed by a player at (row, col)."""
    if st.session_state.board[row][col] != EMPTY_SYMBOL or st.session_state.winner is not None:
        return

    player = st.session_state.current_player
    st.session_state.board[row][col] = player

    # Check for victory
    if check_victory(st.session_state.board, player):
        st.session_state.winner = player
        st.session_state.scores[player] += 1
        return

    # Switch turns
    st.session_state.current_player = (
        PLAYER2_SYMBOL if player == PLAYER1_SYMBOL else PLAYER1_SYMBOL
    )

    # Trigger Bot move if applicable
    if (
        st.session_state.game_mode == "Human vs Bot"
        and st.session_state.current_player == PLAYER2_SYMBOL
        and st.session_state.winner is None
    ):
        bot_move = get_bot_move(
            st.session_state.board, PLAYER2_SYMBOL, PLAYER1_SYMBOL
        )
        if bot_move:
            b_row, b_col = bot_move
            st.session_state.board[b_row][b_col] = PLAYER2_SYMBOL
            if check_victory(st.session_state.board, PLAYER2_SYMBOL):
                st.session_state.winner = PLAYER2_SYMBOL
                st.session_state.scores[PLAYER2_SYMBOL] += 1
            else:
                st.session_state.current_player = PLAYER1_SYMBOL


# 1. Page Configuration & Custom CSS Injection
st.set_page_config(page_title="Bridg-It Game", page_icon="🌉")

# CSS to remove low opacity/blurriness from disabled Streamlit buttons
st.markdown("""
    <style>
    /* Forces board buttons to maintain full opacity even when disabled */
    div[data-testid="stButton"] > button:disabled {
        opacity: 1.0 !important;
        color: inherit !important;
        cursor: not-allowed;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌉 Bridg-It Game")

# 2. State Initialization
init_game_state()

# 3. Sidebar Configuration
st.sidebar.header("Game Settings")
st.sidebar.radio(
    "Select Game Mode:",
    options=["Human vs Human", "Human vs Bot"],
    key="game_mode",
    on_change=on_game_mode_change  # Resets the board when changing game mode
)

col_btn1, col_btn2 = st.sidebar.columns(2)
with col_btn1:
    if st.sidebar.button("Reset Game", on_click=reset_game, use_container_width=True):
        st.sidebar.success("Board reset!")
with col_btn2:
    if st.sidebar.button("Reset Scores", on_click=reset_scores, use_container_width=True):
        st.sidebar.info("Scores reset!")

# 4. Scoreboard Header
col1, col2 = st.columns(2)
with col1:
    st.metric(
        label=f"Player 1 ({PLAYER1_SYMBOL}) - Top/Bottom",
        value=st.session_state.scores[PLAYER1_SYMBOL]
    )
with col2:
    player2_label = "Bot" if st.session_state.game_mode == "Human vs Bot" else "Player 2"
    st.metric(
        label=f"{player2_label} ({PLAYER2_SYMBOL}) - Left/Right",
        value=st.session_state.scores[PLAYER2_SYMBOL]
    )

# 5. Victory Banner or Current Turn Indicator
if st.session_state.winner:
    st.success(f"🎉 **Player {st.session_state.winner} WINS THE GAME!** 🎉")
    st.balloons()
else:
    st.info(f"**Current Turn:** Player {st.session_state.current_player}")

# 6. Render Board Grid
board_size = len(st.session_state.board)
for r in range(board_size):
    cols = st.columns(board_size)
    for c in range(board_size):
        cell_value = st.session_state.board[r][c]
        
        # Uses exact board symbol (🟩 for empty, 🔴 or 🟡 for played cells)
        display_label = cell_value
        is_disabled = (cell_value != EMPTY_SYMBOL) or (st.session_state.winner is not None)
        
        cols[c].button(
            label=display_label,
            key=f"cell_{r}_{c}",
            on_click=handle_move,
            args=(r, c),
            disabled=is_disabled,
            use_container_width=True
        )