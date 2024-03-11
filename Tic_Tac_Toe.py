# PE1---Tic-Tac-Toe
# Python Essentials - Part 1 (Basics)
# 4.7.2.1 PROJECT: Tic-Tac-Toe
# https://edube.org/learn/pe-1/project-tic-tac-toe-4

def display_board(board, mode=0):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    if size == 3:
        # For a case number on only one digit
        caseSize = 7
        sizeNumber = 1
        trimArroundNumber = 3
    else:
        # For a case number with one or two digits
        caseSize = 8
        sizeNumber = 2
        trimArroundNumber = 3
        
    if mode == 1:
        Line_Full = (("+" + "-" * caseSize) * size) + "+"
        Line_Empty = (("|" + " " * caseSize) * size) + "|"
        for row in board:
            print(Line_Full)
            print(Line_Empty)
            Line_Data = "|"
            for col in row:
                Line_Data += (" " * trimArroundNumber) + str(col).ljust(sizeNumber) + (" " * trimArroundNumber) + "|"
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
        print(">> Enter your move (or '", quitKeyword, "' to exit game): ", sep='', end='')
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
            rowBoard = (moveValue - 1) // size
            colBoard = (moveValue - 1) % size
            board[rowBoard][colBoard] = tickPlayer
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
    # Check for rows
    for row in board:
        if row.count(sign) == size:
            return True
    # Check for columns
    for colNum in range(size):
        colSum = 0
        for rowNum in range(size):
            if board[rowNum][colNum] == sign:
                colSum += 1
        if colSum == size:
            return True
    # Check for diagonals
    # Check for diagonal Top Left corner to Bottom Right corner
    print("victory_for sign:", sign, " - Check for diagonal Top Left corner to Bottom Right corner - to be defined")
    # Check for diagonal Top Right corner to Bottom Left corner
    print("victory_for sign:", sign, " - Check for diagonal Top Right corner to Bottom Left corner - to be defined")
    
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("draw_move - to be defined")

def checkTheGame(board):
    global gameStatus
    global freeSquares
    if victory_for(board, tickComputer):
        print("You lose!")
        return gameComputerWin
    elif victory_for(board, tickPlayer):
        print("You win!")
        return gameYouWin
    elif len(freeSquares) == 0:
        print("The game ends with a tie!")
        return gameTie
    else:
        return gameContinue

# Constants
quitKeyword = "exit"
tickComputer = "X"
tickPlayer = "O"
gameStart = "start"
gameContinue = "continue"
gameTie = "tie"
gameYouWin = "YouWin"
gameComputerWin = "ComputerWins"

# Ask for the size
size = 0
while size == 0:
    print(">> Enter the size of the game (type ENTER for the default = 3 or type '", quitKeyword, "' to exit game): ", sep='', end='')
    inputValue = input()
    if inputValue.lower() == quitKeyword:
            print("Good bye.")
            exit(0)
    elif inputValue == "":
        size = 3
    elif not inputValue.strip().isdigit():
        print("Enter an integer!")
    else:
        try:
            size = int(inputValue)
        except:
            size = 3

fullSize = size ** 2

# The infinite loop
gameStatus = gameStart
exitCode = None
while gameStatus == gameStart or gameStatus == gameContinue:
    
    # Start the game
    if gameStatus == gameStart:
        print("The game starts.")
        
        # Initialization of the board
        freeSquares = []
        board = [[None for row in range(size)] for col in range(size)]
        caseNumber = 0
        for row in range(size):
            for col in range(size):
                caseNumber += 1
                board[row][col] = caseNumber

        # First move by the computer
        # It always puts its first 'X' in the middle of the board
        board[1][1] = tickComputer

        # Display the board
        display_board(board, 1)

        # Builds the list of all the free squares
        make_list_of_free_fields(board)

    # Move by the player
    exitCode = enter_move(board)
    if exitCode == quitKeyword:
        print("Looser!")
        break
    
    # Builds the list of all the free squares
    make_list_of_free_fields(board)
    
    # Display the board
    display_board(board, 1)
    
    # Check the game
    gameStatus = checkTheGame(board)
    if gameStatus != gameContinue:
        print(">> Play again? Type '", quitKeyword, "' to exit game or any input to continue playing: ", sep='', end='')
        inputValue = input()
        if inputValue.lower() == quitKeyword:
            print("Good bye.")
            break
        else:
            gameStatus = gameStart
            continue
    
    # Move by the computer
    draw_move(board)

