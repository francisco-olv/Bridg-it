# 🌉 Bridg-It Game

A modern, interactive web implementation of the classic **Bridg-It** connection board game built with **Python**, **Streamlit**, and **Pytest**.

---

## 📖 About the Game

The objective of Bridg-It is to build an unbroken path of bridges connecting your assigned opposite boundaries of the board before your opponent does.

### 🎯 Rules & Mechanics:
- **Asymmetric Goals**:
  - 🔴 **Player 1 (Red):** Connects the **Top** boundary to the **Bottom** boundary.
  - 🟡 **Player 2 / Bot (Yellow):** Connects the **Left** boundary to the **Right** boundary.
- **Board Grid**: Played on an $N \times N$ matrix (default $5 \times 5$) composed of fixed player nodes and empty spaces (`🟩`).
- **Game Modes**: Supports both **Human vs Human** and **Human vs Bot** matches.
- **Victory Detection**: Uses Breadth-First Search (BFS) graph traversal algorithms to validate win conditions instantly after every turn.

---

## 🛠️ Tech Stack & Concepts Applied

- **Python 3.12+**: Core business logic, BFS graph search, and bot heuristics using standard libraries (`collections.deque`, `copy`, `random`).
- **Streamlit**: Web interface, session state management, custom CSS styling for high-contrast board state, and score tracking.
- **Pytest**: Comprehensive automated unit testing covering board mechanics, BFS victory validation, and bot logic.
- **Git & GitHub**: Structured feature branch workflow (`feature/*`) with Pull Request code reviews and standard commit conventions.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher installed.
- A virtual environment set up (recommended).

### Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/francisco-olv/Bridg-it.git
   cd Bridg-it
2. **Create and activate your virtual environment (WSL / Linux / macOS):**
    ```bash
    python3 -m venv .venv

    source .venv/bin/activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
5. **Run unit tests:**
    ```bash
    pytest
    ```

## 📂 Project Structure

```text
.
├── app.py              # Streamlit UI, session state & layout rendering
├── board.py            # Board matrix generation, constraints & constants
├── validator.py        # Graph traversal (BFS) for asymmetric victory checks
├── bot.py              # Automated move selection & win/block heuristics
├── test_board.py       # Unit tests for board mechanics
├── test_validator.py   # Unit tests for BFS graph algorithms
├── test_bot.py         # Unit tests for bot logic
├── test_game.py        # Integration test suite
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation