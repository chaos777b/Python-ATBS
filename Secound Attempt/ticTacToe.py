 #!/usr/bin/python3
'''
    File name: ticTacToe.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def main():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

    printBoard(theBoard)


if __name__ == '__main__':
    main()