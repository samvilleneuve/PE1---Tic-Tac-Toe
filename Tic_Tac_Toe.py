def display_board(board, mode=0):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    if mode == 1:
        Line_Full = (("+" + "-" * 7) * size) + "+"
        Line_Empty = (("|" + " " * 7) * size) + "|"
        for row in board:
            print(Line_Full)
            print(Line_Empty)
            Line_Data = "|"
            for col in row:
                Line_Data += (" " * 3) + str(col) + (" " * 3) + "|"
            print(Line_Data)
            print(Line_Empty)
        print(Line_Full)
    elif mode == 2:
        for row in board:
            line = ""
            for col in row:
                line += str(col) + " "
            print(line)
    else:
        print(board)
    print()

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    continueInput = True
    while continueInput:
        print("Enter your move (or '", quitKeyword, "' to exit game): ", sep='', end='')
        inputValue = input()
        if inputValue.lower() == quitKeyword:
            return quitKeyword
        elif not inputValue.strip().isdigit():
            print("Enter an integer!")
            continue
        else:
            moveValue = int(inputValue)
        
        # User entered an integer
        if not 1 <= moveValue <= fullSize:
            print("Your value must be greater than 0 and less than", fullSize + 1)
        elif not any(moveValue in row for row in board):
            print("Enter the number of a free square!")
        else:
            # Update board
            # ...
            continueInput = False
    return

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global freeSquares
    freeSquares = []
    for rowNum in range(size):
        for colNum in range(size):
            if isinstance(board[rowNum][colNum], int):
                freeSquares.append((rowNum+1, colNum+1))

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print("to be defined")

def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("to be defined")

# Initialization of the board
quitKeyword = "quit"
size = 3
fullSize = size ** 2
computerTick = "X"
playerTick = "O"
freeSquares = []
board = [[None for row in range(size)] for col in range(size)]
caseNumber = 0
for row in range(size):
    for col in range(size):
        caseNumber += 1
        board[row][col] = caseNumber

# First move by the computer
board[1][1] = computerTick

# Display the board
display_board(board, 1)

make_list_of_free_fields(board)

gameStatus = 1
exitCode = None
while gameStatus == 1 and exitCode != quitKeyword:
    exitCode = enter_move(board)

