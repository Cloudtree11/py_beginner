
theBoard = {};

def printBoard(board):
    print()

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn = 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
