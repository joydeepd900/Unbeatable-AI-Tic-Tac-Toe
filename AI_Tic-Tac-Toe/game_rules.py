def check_win(board, mark):
    # All winning combinations (Rows, Columns, Diagonals)
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for a, b, c in wins:
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True
    return False

def check_draw(board):
    return ' ' not in board
