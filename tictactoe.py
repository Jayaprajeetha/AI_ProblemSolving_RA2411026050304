import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3:(i+1)*3])

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def is_full():
    return " " not in board

def minimax(is_max):
    if check_winner("X"):
        return -1
    if check_winner("O"):
        return 1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def ai_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(False)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    board[move] = "O"

def play():
    while True:
        print_board()
        pos = int(input("Enter position (0-8): "))
        if board[pos] == " ":
            board[pos] = "X"
        else:
            print("Invalid move")
            continue

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if is_full():
            print_board()
            print("Draw!")
            break

play()