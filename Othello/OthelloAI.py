#/usr/bin/python


import time

def make_board(board):
    for i in range(8):
        for c in range(8):
            board[i][c] = " "

def copy_board(board,copy):
    for i in range(8):
        for c in range(8):
            copy[i][c] = board[i][c]
    # makes a copy of the board to find the best possible move for the AI

def set_starting_position(board):
    board[3][3] = "X"
    board[4][4] = "X"
    board[3][4] = "O"
    board[4][3] = "O"
    # sets the starting positions

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
    # if the users inputs is either not ABCDEFGH 123456789 then it will ask the user for another input
    while inputplay[1] not in ("1", "2", "3", "4", "5", "6", "7", "8") or inputplay[0] not in ("A", "B", "C", "D", "E", "F", "G", "H"):
        if player == "X":
            inputplay = input("Mr.X, What is your play A1-H8? ")
        else:
            inputplay = input("Mr.O, What is your play A1-H8? ")

        if inputplay[1] in ("1", "2", "3", "4", "5", "6", "7", "8") and inputplay[0] in ("A", "B", "C", "D", "E", "F", "G", "H"):
            row = int(inputplay[1]) - 1
            column = ord(inputplay[0]) - 65
            # turn the letters into an ascii value and subtracts by the appropriate amount
            move_good = 0
            move_good = check_if_valid_move(board, column, row, player)
            #makes sure the move the user inputed is valid
            if move_good == 0:
                inputplay = "Z0"
            # if it isn't ask the user for another input
            else:
                board[column][row]= player
                letter_change(board, row, column, player)
            # if it is put it in and change the letters in between
def check_if_valid_move(board, column, row, player):

    movement_direction_steps = [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]
    # this is what happens to the cordinates if you move 1 way in each direction
    if player=="X":
        opponent="O"
    else:
        opponent="X"

    valid_move = 0
    if board[column][row] == (" "):
        for direction in range(8):

            if (valid_move == 0):
                # only lopping if valid move is 0 because we are checking to see if it is a valid move
                square_to_examine_row = row
                square_to_examine_column =column
                this_direction_column_chg=movement_direction_steps[direction][0]
                this_direction_row_chg=movement_direction_steps[direction][1]
                # variables that we want to look at and move towards
                might_be_valid_move=0
                end_walk = 0
                while ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                       (square_to_examine_column >= 0) and (square_to_examine_column <= 7) and # keeping it inside the board
                       (end_walk == 0)):

                    square_to_examine_row = square_to_examine_row + this_direction_row_chg
                    square_to_examine_column = square_to_examine_column + this_direction_column_chg

                    if ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                           (square_to_examine_column >= 0) and (square_to_examine_column <= 7)):

                           if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == player)):
                               valid_move = 1
                               end_walk = 1
                               # walking out and seeing if the piece after an oppenents piece is your piece becuase if it is than the move is valid
                               # we do this 8 times so that if you walk out and keep seeing an oppenents piece for 7 tiles but on the 8th tiles you find your piece, it will still work
                           if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == " ")):
                               valid_move = 0
                               end_walk = 1
                               # if it is walking out finds an opponents piece but then finds a space the move is invalid


                           if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] in (" ", player))):
                               end_walk = 1
                               # if it is at the start of walking out and the first thing it hits is a space or a player then the move is invalid

                           if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] == opponent)):
                               might_be_valid_move = 1
                               # if it is at the start of walking out and the first thing it hits is an oppents player then the move might be valid
    return valid_move

def letter_change(board, row, column, player):
    # this code is very similar to the check if valid move code
    movement_direction_steps = [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]
    if player=="X":
        opponent="O"
    else:
        opponent="X"


    actual_flip_list=[]
    # list where all of the letter that will need to be flipped will go
    for direction in range(8):

        valid_move = 0
        square_to_examine_row = row
        square_to_examine_column =column
        this_direction_column_chg=movement_direction_steps[direction][0]
        this_direction_row_chg=movement_direction_steps[direction][1] # this is setting up the walking out part of the code

        might_be_valid_move=0
        end_walk = 0
        possible_flip_list = []
        # list of letter that might be flipped
        this_square = [0,0]

        while ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                (square_to_examine_column >= 0) and (square_to_examine_column <= 7) and
                (end_walk == 0)):

            square_to_examine_row = square_to_examine_row + this_direction_row_chg
            square_to_examine_column = square_to_examine_column + this_direction_column_chg

            if ((square_to_examine_row >= 0) and (square_to_examine_row <= 7) and
                (square_to_examine_column >= 0) and (square_to_examine_column <= 7)):

                this_square = [square_to_examine_column,square_to_examine_row]
                # this_square is the coordinates of the tile(s) that are in the middle of your own two letters
                if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == player)):
                    valid_move = 1
                    end_walk = 1


                if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == " ")):
                    valid_move = 0
                    end_walk = 1

                if ((might_be_valid_move==1) and (board[square_to_examine_column][square_to_examine_row] == opponent)):
                    possible_flip_list.append(this_square)
                    # if there might be a valid move and the next tile that you move out into happens to be the opponent that it adds the coordinates to the list
                if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] in (" ", player))):
                    end_walk = 1

                if ((might_be_valid_move==0) and (board[square_to_examine_column][square_to_examine_row] == opponent)):
                    possible_flip_list.append(this_square)
                    might_be_valid_move = 1
                    # if the program is just starting to walk out and the tile it hits is a oppenent then it adds the coordinates to the list
            if (valid_move == 1):
                for i in range(len(possible_flip_list)):
                    actual_flip_list.append(possible_flip_list[i])
                # if the move was valid it adds all of the numbers in pos_flip_list to actual_flip_list
    for i in range (len(actual_flip_list)):
        board[actual_flip_list[i][0]][actual_flip_list[i][1]] = player
        # then it flips the letters

def computer_play(board, computer_player):
    # using a copy of the board to find the best possible tile to play each turn
    test_board = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "]]
    found_move = 0
    winner=""
    gamenotover=1
    px_score=0
    po_score=0
    best_computer_score = 0
    # if it can go into a corner it goes there automatically, cause that is probably the best play
    if (check_if_valid_move(board, 0, 0, computer_player) ==1):
        found_move = 1
        chosen_computer_row = 0
        chosen_computer_column = 0

    elif (check_if_valid_move(board, 0, 7, computer_player) ==1):
        found_move = 1
        chosen_computer_row = 7
        chosen_computer_column = 0

    elif (check_if_valid_move(board, 7, 7, computer_player) ==1):
        found_move = 1
        chosen_computer_row = 7
        chosen_computer_column = 7

    elif (check_if_valid_move(board, 7, 0, computer_player) ==1):
        found_move = 1
        chosen_computer_row = 0
        chosen_computer_column = 7

    else:
        for i in range(8):
            for c in range(8):
                poss_comp_move = 0
                poss_comp_move = check_if_valid_move(board, c, i, computer_player)
                # goes through each tile to see if it is a valid move or not
                if (poss_comp_move ==1):
                    copy_board(board, test_board)
                    test_board[c][i] = computer_player
                    letter_change(test_board,i,c,computer_player)
                    gamenotover, px_score, po_score = check_for_end(test_board, winner)
                    # goes through each tiles places an O in copy board and sees how much its score went up
                    if (computer_player == "X"):
                        comp_score_this_move = px_score
                    else:
                        comp_score_this_move = po_score

                    if (comp_score_this_move > best_computer_score):
                        best_computer_score = comp_score_this_move
                        chosen_computer_row = i
                        chosen_computer_column = c

    board[chosen_computer_column][chosen_computer_row]= computer_player
    letter_change(board, chosen_computer_row, chosen_computer_column, computer_player)
    # the computer finds the tile with the highest score output and places an O there
def does_player_have_any_move(board, player):
# checks to see if the any player, whether its the computer or the human, has a move or can't play anymore
    cell_valid_moves = 0
    for i in range(8):
        for c in range(8):
            if (cell_valid_moves == 0):
                cell_valid_moves = check_if_valid_move(board, c, i, player)
    return cell_valid_moves

def check_for_end(board, winner):

    winner = " "
    px_score = 0
    po_score = 0
    gamenotover = 0
    for i in range(8): # keeps count of the score
        for c in range(8):
            if board[c][i] == "X":
                px_score = px_score + 1
            if board[c][i] == "O":
                po_score = po_score + 1
            if board[c][i] == " ":
                gamenotover = 1

    if (gamenotover == 0): # returns which who ever won
        if px_score > po_score:
            winner= "X"
        if px_score < po_score:
            winner = "Computer"
        if px_score == po_score:
            winner = "T"

    return (gamenotover, px_score, po_score)

play_again = "y"

board= [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
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
    player_has_no_move = 0
    while (gamenotover == 1):
        does_move_exist = does_player_have_any_move(board, "X")
        if (does_move_exist == 1):
            get_move(board, "X")
            print_board(board)
            # if there is a move, get the move from X
        else:
            player_has_no_move = 1
            # if there is no more moves then the game stops


        if (player_has_no_move == 0):

            does_move_exist = does_player_have_any_move(board, "O")

            if (does_move_exist == 1):
                print("Computer is thinking...")
                time.sleep(1.5)
                computer_play(board,"O")
                print_board(board)
                # computer makes play
            else:
                player_has_no_move = 1
                # else no more move, and it shows whoever won

        gamenotover, px_score, po_score = check_for_end(board, winner)
        if (player_has_no_move == 1):
            gamenotover = 0

        print ("Computer score is " + str(po_score))
        print ("Mr.X score is " + str(px_score))

        if gamenotover == 0:
            if (winner != "T"): #T=tie
                print (winner + " won!")
            else:
                print ("It's a tie!")

                # ask to see if the user wants to play again
    play_again = input("Do you want to play again? y/n")
