# Tic Tac Toe

boardSize = 3
board = [" " for i in range(boardSize ** 2)]


def insert_letter(letter, pos):
    board[pos] = letter


# returns 1 if space is free
def space_is_free(pos):
    return board[pos] == " "


def print_board(boardSize, board):
    for i in range(boardSize):
        for j in range(boardSize):
            print("| {}".format(board[i * boardSize + j]), end=" ")
        print("|")


def is_winner(bo, letter):
    return (bo[6] == letter and bo[7] == letter and bo[8] == letter) or \
           (bo[3] == letter and bo[4] == letter and bo[5] == letter) or \
           (bo[0] == letter and bo[1] == letter and bo[2] == letter) or \
           (bo[0] == letter and bo[3] == letter and bo[6] == letter) or \
           (bo[1] == letter and bo[4] == letter and bo[7] == letter) or \
           (bo[2] == letter and bo[5] == letter and bo[8] == letter) or \
           (bo[0] == letter and bo[4] == letter and bo[8] == letter) or \
           (bo[2] == letter and bo[4] == letter and bo[6] == letter)


def player_move():
    run = True
    while run:
        move = input("Select a position to place an X (0-8): ")
        try:
            move = int(move)
            if move >= 0 and move <= 8:
                if space_is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print("Space isn't free")
            else:
                print("Please type a number within the range")
        except:
            print("type a number")


def player2_move():
    run = True
    while run:
        move = input("Select a position to place an O (0-8): ")
        try:
            move = int(move)
            if move >= 0 and move <= 8:
                if space_is_free(move):
                    run = False
                    insert_letter("O", move)
                else:
                    print("Space isn't free")
            else:
                print("Please type a number within the range")
        except:
            print("type a number")


def comp_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " "]
    move = 0

    for letter in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if is_winner(boardCopy, letter):
                move = i
                return move

    if 4 in possibleMoves:
        move = 4
        return move

    openCorners = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            openCorners.append(i)

    if len(openCorners) > 0:
        move = select_random(openCorners)
        return move

    openEdges = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            openEdges.append(i)

    if len(openEdges) > 0:
        move = select_random(openEdges)

    return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def board_is_full(board):
    return not(board.count(" ") > 0)


def main():
    print("Welcome to Tic Tac Toe")
    print_board(boardSize, board)

    while not (board_is_full(board) or is_winner(board, "X") or is_winner(board, "O")):
        if not (is_winner(board, "O")):
            player_move()
            print_board(boardSize, board)

        if not (is_winner(board, "X")):
            #player2_move()
            move = comp_move()

            if move != 0:
                insert_letter("O", move)
                print("Computer placed an O in {} :".format(move))
            else:
                print("Not able to come up with a move")


            print_board(boardSize, board)

    # print match result
    if is_winner(board, "X"):
        print('X\'s won this time')

    if is_winner(board, "O"):
        print('O\'s won this time')

    if board_is_full(board):
        print("Tie")


main()