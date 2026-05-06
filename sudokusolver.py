def print_board(board):
    for row in board:
        print(row)

def is_valid(board, row, col, num):
    # row
    if num in board[row]:
        return False

    # column
    for i in range(9):
        if board[i][col] == num:
            return False

    # box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

board = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

if solve(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution")