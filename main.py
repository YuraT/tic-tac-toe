# Tic Tac Toe
#initialize board size
boardSize = " "
while (not(boardSize.isdigit())):
    boardSize = input("Please type in the board size: ")

boardSize = int(boardSize)

#initialize board
board = [[" " for i in range(boardSize)] for j in range(boardSize)]

#functions

#checks if space is free at coordinates
def space_is_free(pos_x, pos_y):
    return board[pos_y][pos_x] == " "

#inserts letter at given coordinates
def insert_letter(letter, pos_x, pos_y):
    board[pos_y][pos_x] = letter

#prints board
def print_board(boardSize, board):
    for i in range(boardSize):
        for j in range(boardSize):
            print("| {}".format(board[i][j]), end=" ")
        print("|")

#checks if letter is the same in row/column/diagonals
def is_winner(board, letter):
    winner = False #main bool variable that is returned
    main_diagonal = True #main diagonal bool var
    secondary_diagonal = True #secondary diagonal bool var
    for i in range(boardSize):
        if board[i][i] != letter: #main diagonal check
            main_diagonal = False 
        if board[boardSize - i - 1][boardSize - i - 1] != letter: #secondary diagonal check
            secondary_diagonal = False

        row = True #checks row every i cycle
        column = True #checks column every i cycle
        for j in range(boardSize):
            if board[i][j] != letter: #row check
                row = False
            if board[j][i] != letter: #column check
                column = False

        winner = winner or row or column #winner == true if any row or column == true
    winner = winner or main_diagonal or secondary_diagonal #winner == true if any diagonal == true
    return winner

def player_move(letter):
    run = True
    while run:
        move = []
        while len(move) != 2: #x and y position input into array, check for length == 2
            print()
            move = input("Select x and y position to place an {} (0-{}, two numbers in line):".format(letter, boardSize-1, end= " ")).split()
        try:
            move[0] = int(move[0])
            move[1] = int(move[1])
            if move[0] >= 0 and move[0] < boardSize and move[1] >= 0 and move[1] < boardSize:
                if space_is_free(move[0], move[1]):
                    run = False
                    insert_letter(letter, move[0], move[1])
                else:
                    print("Space isn't free")
            else:
                print("Please type a number within the range")
        except:
            print("Type a number")


def board_is_full(board):
    for i in range(boardSize):
        if board[i].count(" ") > 0:
            return False
    return True


def main():
    print("Welcome to Tic Tac Toe")
    print_board(boardSize, board)

    while not (board_is_full(board) or is_winner(board, "X") or is_winner(board, "O")):
        if not (is_winner(board, "O")):
            player_move("X")
            print_board(boardSize, board)

        if not (is_winner(board, "X")):
            player_move("O")

            print_board(boardSize, board)

    # print match result
    if is_winner(board, "X"):
        print('X\'s won this time')

    if is_winner(board, "O"):
        print('O\'s won this time')

    if board_is_full(board):
        print("Tie")

main()
