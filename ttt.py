import os

board = [ ["x", "_", "o"],
          ["_", "_", "_"],
          ["_", "_", "_"]
        ] 

def printBoard(board):
    for row in board:
        print(row)
    print()


def initBoard(board):
    board = [["_" for i in range(3)] for i in range(3)]
    return board

def populateBoard(board, inputPosition, piece):
    match inputPosition:
        case 1:
            board[0][0] = piece
        case 2:
            board[0][1] = piece
        case 3:
            board[0][2] = piece
        case 4:
            board[1][0] = piece
        case 5:
            board[1][1] = piece
        case 6:
            board[1][2] = piece
        case 7:
            board[2][0] = piece
        case 8:
            board[2][1] = piece
        case 9:
            board[2][2] = piece            
    return board

def getValidInput():
    inputPosition = 0
    while inputPosition not in range(1,10):
        try: 
            inputPosition = int(input("Enter a position 1-9: "))
        except ValueError:
            print("Please enter a number")
    return inputPosition

# Main program
os.system("cls")
board = initBoard(board)
printBoard(board)

inputPosition = getValidInput()

board = populateBoard(board, inputPosition, 'x')
printBoard(board)