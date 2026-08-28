import streamlit as st
from board import create_board, PLAYER1_SYMBOL, PLAYER2_SYMBOL

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
    """Resets the board and current turn while preserving score and game mode."""
    st.session_state.board = create_board(size=5)
    st.session_state.current_player = PLAYER1_SYMBOL
    st.session_state.winner = None

# 1. Page Configuration
st.set_page_config(page_title="Bridg-It Game", page_icon="🌉")
st.title("🌉 Bridg-It Game")

# 2. State Initialization
init_game_state()

# 3. Sidebar Configuration
st.sidebar.header("Game Settings")
game_mode = st.sidebar.radio(
    "Select Game Mode:",
    options=["Human vs Human", "Human vs Bot"],
    key="game_mode"
)

if st.sidebar.button("Reset Game", on_click=reset_game):
    st.sidebar.success("Game reset successfully!")

# 4. Scoreboard Header
col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"Player 1 ({PLAYER1_SYMBOL})", value=st.session_state.scores[PLAYER1_SYMBOL])
with col2:
    st.metric(label=f"Player 2 / Bot ({PLAYER2_SYMBOL})", value=st.session_state.scores[PLAYER2_SYMBOL])

st.write(f"**Current Turn:** Player {st.session_state.current_player}")