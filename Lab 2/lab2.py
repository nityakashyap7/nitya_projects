"""
Nitya Kashyap
Lab 2
CIS 41A
1/21/2023
Description: simplified version of battleships
"""

import random
MIN = 2
MAX = 4


# def getNum(inputType, size=0):
#     """
#     Gets valid input from user for board size, row and column guesses
#     :param inputType: string "row"/"column" or "board size"
#     :param size: integer size of board (if already established).
#     At first, there won't be an established size, so size default value is zero
#     :return: validated integer value of either board size, row, or column
#     """
#     obtainingInput = True
#
#     '''should not have to repeat the same block of code to read input as the above block.
#     This defeats the purpose of writing a function to do the same task.'''
#
#     if inputType == "row" or inputType == "column":
#         while obtainingInput:
#             coordinate = input(f"Enter a {inputType}: ")
#             if coordinate.isdigit() and 1 <= int(coordinate) <= size:
#                 coordinate = int(coordinate)
#                 obtainingInput = False
#             else:
#                 print(f"invalid prompt. enter an integer from 1 to {size}")
#         return coordinate
#     else:
#         while obtainingInput:
#             boardSize = input("Enter size of board: ")
#             if boardSize.isdigit() and MIN <= int(boardSize) <= MAX:
#                 boardSize = int(boardSize)
#                 obtainingInput = False
#             else:
#                 print(f"invalid prompt. enter an integer from {MIN} to {MAX}")
#         return boardSize


# if the user has not yet made a guess,
# the board still needs to print out the board
# but without any "X"

# revised getNum
def getNum(inputType, low, high):
    obtainingInput = True
    while obtainingInput:
            num = int(input(inputType))
            if low <= num <= high:
                return
'''
def printBoard(size, xCoord = None, yCoord = None):
    """
    Prints the board layout to the console.
    If user correctly guessed ship location,
    an 'X' is printed to indicate their success.
    :param size: integer value board size
    :param xCoord: integer value row number
    :param yCoord: integer value column number
    :return: None
    """
    # print row of column numbers
    print(" ", end="")
    for i in range(1,size+1):
        print(" "*2, i, end="")

    # first dashed line
    print("\n   " + "-"*(size*4))

    # each row with row number + boxes
    # followed by a row of dashes
    for x in range (1, size+1):
        print(x, " ", end="")
        for y in range(1, size+2):
            if y == yCoord and x == xCoord:
                print("| X ", end="")
            else: print("|   ", end="")
        print("\n   " + "-" * (size * 4))

def hideShip(size):
    """
    Generates random coordinates for ship to be hidden at.
    :param size: integer value board size
    :return: tuple of row and column coordinates
    """
    row = random.randint(1, size)
    column = random.randint(1, size)
    # print(row, column) # for testing purposes
    return (row, column)

def play():
    """
    Executes one game of battleship.
    The user keeps guessing until they've hit the ship.
    Number of attempts is recorded.
    :return: None
    """
    # boardSize = getNum("board size")    # dont do this! pass in whole prompt
    boardSize = getNum("Enter size of board: ", 2, 4)
    shipLocation = hideShip(boardSize)
    gameOver = False
    numTries = 0
    while not gameOver:
        printBoard(boardSize)
        guessedRow = getNum("row", boardSize)
        guessedColumn = getNum("column", boardSize)
        numTries += 1
        if shipLocation[0] == guessedRow and shipLocation[1] == guessedColumn:
            printBoard(boardSize, guessedRow, guessedColumn)
            print(f"You got it in {numTries} tries!")
            gameOver = True

def main():
    random.seed() # YOU FORGOT TO SEED RANDOM!! MAKE SURE TO CHECK OFF ALL SPECS BEFORE SUBMITTING!!
    keepPlaying = True
    while keepPlaying:
        play()
        userChoice = input("Continue? y/n: ").lower()
        if userChoice != "y":
            keepPlaying = False


main()
'''