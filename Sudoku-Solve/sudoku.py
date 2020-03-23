board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def backTrack(board):
    find = find_empty(board)
    if not find:
        return True;
    else:
        row, col = find;
    for i in range(1,10):
        if(check_number(board,i,(row,col))):
            board[row][col] = i;
            if(backTrack(board)):
                return True
            board[row][col] = 0;
    return False;""

def check_number(board, number, position):
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    boxX = position[1] // 3
    boxY = position[0] // 3
    for i in range(boxY*3, boxY*3 + 3):
        for j in range(boxX * 3, boxX*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True

def print_board(board):
    for row in range(len(board)):
        if(row % 3 == 0 and row != 0):
            print("------------------------");
        for col in range(len(board[0])):
            if(col % 3 == 0 and col != 0):
                print(" | ", end="");

            if(col == 8):
                print(board[row][col]);
            else:
                print(str(board[row][col]) + " ", end="");

def find_empty(board):
    for emptyR in range(len(board)):
        for emptyC in range(len(board[0])):
            if(board[emptyR][emptyC] == 0):
                return emptyR, emptyC
    return None;
print_board(board)
backTrack(board)
print("\n")
print("\n")
print_board(board)
