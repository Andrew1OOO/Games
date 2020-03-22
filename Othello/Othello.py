def make_board(board):
    for i in range(8):
        for c in range(8):
            board[i][c] = " "


def set_starting_position(board):
    board[3][3] = "X"
    board[4][4] = "X"
    board[3][4] = "O"
    board[4][3] = "O"


def print_board(board):
    print(" |A|B|C|D|E|F|G|H|")
    print(" |---------------|")
    for i in range(8):
        rowstring = str(i + 1)
        for c in range(8):
            rowstring = rowstring + "|" + board[c][i]
        print(rowstring + "|")
        print(" |---------------|")

def get_move(board, player):
    row = 0
    column = 0
    inputplay = "Z0"
    while inputplay[1] not in ("1", "2", "3", "4", "5", "6", "7", "8") or inputplay[0] not in ("A", "B", "C", "D", "E", "F", "G", "H"):
        if player == "X":
            inputplay = input("Mr.X, What is your play A1-H8? ")
        else:
            inputplay = input("Mr.O, What is your play A1-H8? ")

        if inputplay[1] in ("1", "2", "3", "4", "5", "6", "7", "8") and inputplay[0] in ("A", "B", "C", "D", "E", "F", "G", "H"):
            row = int(inputplay[1]) - 1
            column = ord(inputplay[0]) - 65

            move_good = 0
            move_good = check_if_valid_move(board, column, row, player)

            if move_good == 0:
                inputplay = "Z0"
            else:
                board[column][row]= player
                letter_change(board, row, column, player)

def check_if_valid_move(board, column, row, player):

    movement_direction_steps = [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]
    if player=="X":
        opponent="O"
    else:
        opponent="X"

    valid_move = 0
    if board[column][row] == (" "):
        for direction in range(8):

            if (valid_move == 0):

                square_to_examine_row = row
                square_to_examine_column =column
                this_direction_column_chg=movement_direction_steps[direction][0]
                this_direction_row_chg=movement_direction_steps[direction][1]

                might_be_valid_move=0
                end_walk = 0
                while ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                       (square_to_examine_column >= 0) and (square_to_examine_column <= 7) and
                       (end_walk == 0)):

                    square_to_examine_row = square_to_examine_row + this_direction_row_chg
                    square_to_examine_column = square_to_examine_column + this_direction_column_chg

                    if ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                           (square_to_examine_column >= 0) and (square_to_examine_column <= 7)):

                           if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == player)):
                               valid_move = 1
                               end_walk = 1

                           if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == " ")):
                               valid_move = 0
                               end_walk = 1

                           if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] in (" ", player))):
                               end_walk = 1

                           if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] == opponent)):
                               might_be_valid_move = 1

    return valid_move

def letter_change(board, row, column, player):
    movement_direction_steps = [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]
    if player=="X":
        opponent="O"
    else:
        opponent="X"



    actual_flip_list=[]
    for direction in range(8):

        valid_move = 0
        square_to_examine_row = row
        square_to_examine_column =column
        this_direction_column_chg=movement_direction_steps[direction][0]
        this_direction_row_chg=movement_direction_steps[direction][1]

        might_be_valid_move=0
        end_walk = 0
        possible_flip_list = []
        this_square = [0,0]
        while ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                (square_to_examine_column >= 0) and (square_to_examine_column <= 7) and
                (end_walk == 0)):

            square_to_examine_row = square_to_examine_row + this_direction_row_chg
            square_to_examine_column = square_to_examine_column + this_direction_column_chg

            if ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                (square_to_examine_column >= 0) and (square_to_examine_column <= 7)):

                this_square = [square_to_examine_column,square_to_examine_row]

                if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == player)):
                    valid_move = 1
                    end_walk = 1

                if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == " ")):
                    valid_move = 0
                    end_walk = 1

                if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == opponent)):
                    possible_flip_list.append(this_square)

                if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] in (" ", player))):
                    end_walk = 1

                if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] == opponent)):
                    possible_flip_list.append(this_square)
                    might_be_valid_move = 1

            if (valid_move == 1):
                for i in range(len(possible_flip_list)):
                    actual_flip_list.append(possible_flip_list[i])

    for i in range (len(actual_flip_list)):
        board[actual_flip_list[i][0]][actual_flip_list[i][1]] = player


def check_for_end(board, winner):

    winner = " "
    px_score = 0
    po_score = 0
    gamenotover = 0
    for i in range(8):
        for c in range(8):
            if board[c][i] == "X":
                px_score = px_score + 1
            if board[c][i] == "O":
                po_score = po_score + 1
            if board[c][i] == " ":
                gamenotover = 1

    if (gamenotover == 0):
        if px_score > po_score:
            winner= "X"
        if px_score < po_score:
            winner = "O"
        if px_score == po_score:
            winner = "T"

    return (gamenotover, px_score, po_score)

play_again = "y"

board= [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " "
    , " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]]

px_score = 0
po_score = 0
winner = " "


while (play_again=="y"):
    make_board(board)
    set_starting_position(board)
    print_board(board)


    gamenotover = 1
    while (gamenotover == 1):
        get_move(board, "X")
        print_board(board)


        get_move(board, "O")
        print_board(board)

        gamenotover, px_score, po_score = check_for_end(board, winner)

        print ("Mr.O score is " + str(po_score))
        print ("Mr.X score is " + str(px_score))

        if gamenotover == 0:
            if (winner != "T"):
                print (winner+" won!")
            else:
                print ("It's a tie!")


    play_again = input("Do you want to play again? y/n")
