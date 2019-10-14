
board = [[" "]*8 for row in range(8)]
currentplayer = None
darkplayer = True

def currentboard():
    rownum = 0
    print('  | 1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |')
    for row in board:
        rownum += 1
        print(rownum, end=' ')
        print(row)

def createpieces():
    global board    
    for row in range(0,8):
        if row <= 2:
            if row % 2 == 0:
                for column in range (1,8,2):
                    board[row][column] = 'O'
            else:
                for column in range (0,8,2):
                    board[row][column] = 'O'
        elif row >= 5:
            if row % 2 == 0:
                for column in range (1,8,2):
                    board[row][column] = 'X'
            else:
                for column in range (0,8,2):
                    board[row][column] = 'X'

def playerturn(darkplayer):
    global currentplayer
    if darkplayer:
        currentplayer = "X"
        print('\nIt\'s ' + currentplayer + ' Turn')
    else:
        currentplayer = "O"
        print('\nIt\'s ' + currentplayer + ' Turn')

def pickpiece():
    x, y = input('Select the coordiantes of the piece you\'d like to move (Example: 1 2)\nCoordinates: ').split()
    if board[int(x) - 1][int(y) - 1] == currentplayer:        
        movepiece(x, y)
    else:
        print('WAIT! That\'s not one of your pieces or that\'s an empty slot. Try again.\n')
        pickpiece()

def movepiece(x, y):
    print('You have selected coordinates ' + x + ' ' + y  + '.')
    print('Where would you like to move your piece: diagonally to the left or diagonally to the right?')    
    direction = input('Choose Left or Right\nDirection: ').capitalize()
    if direction == 'Left':
        print('You chose ' + direction)
    elif direction == 'Right':
        print('You chose ' + direction)
    else:
        print('Unspecified direction. Try again.\n')
        movepiece(x, y)

createpieces()

currentboard()
playerturn(darkplayer)
pickpiece()