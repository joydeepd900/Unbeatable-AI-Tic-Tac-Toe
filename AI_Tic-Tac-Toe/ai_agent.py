from game_rules import check_win, check_draw

def minimax(board, depth, is_maximizing):
    # Base cases: AI wins (+1), Human wins (-1), Draw (0)
    if check_win(board, 'O'): return 1
    if check_win(board, 'X'): return -1
    if check_draw(board): return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -1000
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
