import streamlit as st

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = [" " for _ in range(9)]

board = st.session_state.board

# Check winner
def check_winner(b, player):
    win_positions = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]
    for a,b_,c in win_positions:
        if b[a] == b[b_] == b[c] == player:
            return True
    return False

# Minimax algorithm
def minimax(b, is_max):
    if check_winner(b, "X"):
        return 1
    if check_winner(b, "O"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = 100
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

# Best move for AI
def best_move():
    best_val = -100
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            val = minimax(board, False)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i
    return move

# UI
st.title("Tic Tac Toe AI")

cols = st.columns(3)

for i in range(9):
    if cols[i % 3].button(board[i], key=i):
        if board[i] == " ":
            board[i] = "O"

            if not check_winner(board, "O"):
                move = best_move()
                if move != -1:
                    board[move] = "X"

# Display result
if check_winner(board, "O"):
    st.success("You Win 🎉")
elif check_winner(board, "X"):
    st.error("AI Wins 🤖")
elif " " not in board:
    st.warning("Draw")

# Reset button
if st.button("Reset Game"):
    st.session_state.board = [" " for _ in range(9)]
