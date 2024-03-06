def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
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

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    print("to be defined")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    print("to be defined")

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print("to be defined")

def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("to be defined")

size = 3
board = [[None for row in range(size)] for col in range(size)]
caseNumber = 0
for row in range(size):
    for col in range(size):
        caseNumber += 1
        board[row][col] = caseNumber
board[1][1] = "X"
display_board(board)