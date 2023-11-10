import os

BOARD = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' '] 
MESSAGE = """Welcome to Tic Tac Toe!
Player 1 is X and Player 2 is O
The board is numbered like this:
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 
To place your symbol, enter the number of the square you want to place it in
Player 1 goes first

----------------------------------------------------------------------------
"""


def display_board(BOARD):
    for i in range(0, 9, 3):
        print(f' {BOARD[i]} | {BOARD[i+1]} | {BOARD[i+2]}')
        if i < 6:
            print('---|---|---')


def display():
    os.system('cls')
    print(MESSAGE)
    print('Current board:')
    display_board(BOARD)


def board_check(BOARD, i):
    if i > 3:
        for j in range(0, 9, 3):
            if BOARD[j] == BOARD[j+1] == BOARD[j+2] != ' ':
                display()
                print(f'Player {i%2+1} wins!')
                return True
        for j in range(3):
            if BOARD[j] == BOARD[j+3] == BOARD[j+6] != ' ':
                display()
                print(f'Player {i%2+1} wins!')
                return True
        if BOARD[0] == BOARD[4] == BOARD[8] != ' ':
            display()
            print(f'Player {i%2+1} wins!')
            return True
        if BOARD[2] == BOARD[4] == BOARD[6] != ' ':
            display()
            print(f'Player {i%2+1} wins!')
            return True
    if i == 8:  
        display()
        print('Tie!')
        return True
    return False


def pos_check(pos):
    try:
        pos = int(pos)
        if 1 <= pos <= 9:
            if BOARD[pos-1] != ' ':
                return 'That cell is not empty, try another cell'
                # print('That cell is not empty, try another cell')
                # return None
            return pos
        else:
            return 'Invalid position, must be between 1 and 9'
            # print('Invalid position, must be between 1 and 9')
            # return None
    except ValueError:
        return 'Invalid position, must be a number'
        # print('Invalid position, must be a number')
        # return None


def TicTakToe():
    pos = 0
    i = 0
    while True:
        display()

        if i%2 == 0:
            print('Player 1 turn (X)')
        else:
            print('Player 2 turn (O)')

        if type(pos) is str:
            print(pos)

        pos = input('Enter a position: ')
        
        pos = pos_check(pos)

        if type(pos) is str:
            continue

        BOARD[pos-1] = 'X' if i%2 == 0 else 'O' # type: ignore

        b_ch = board_check(BOARD, i)
        if b_ch:
            break
        
        i += 1
    

if __name__ == '__main__':
    TicTakToe()