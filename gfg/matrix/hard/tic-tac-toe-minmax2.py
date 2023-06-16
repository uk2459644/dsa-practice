"""
Find the best move:

We shall introduce a new function called findBestMove(). This function evaluates all the
available moves using minimax() and then returns the best move the mximizer can make.

The pseudocode is  as follow:

function findBestMove(board):
    bestmove=Null

    for each move in board:
       if current move is better than bestmove:
           bestmove= current move
    return bestmove

"""
# program to find the next optimal move for a player
player, opponent = 'x','o'

# This function returns true if there are moves remaining on the board.
# If returns false if there are no moves left to play.

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                return True
    
    return False

def evaluate(b):
    # checking for rows for x or 0 visctory
    for row in range(3):
        if (b[row][0]==b[row][1] and b[row][1]==b[row][2]):
            if b[row][0]==player:
                return 10
            elif b[row][0]==player:
                return -10
    
    # Checking for columns for x or o victory
    for col in range(3):
        if b[0][col]==b[1][col] and b[1][col]==b[2][col]:
            if b[0][col]==player:
                return 10
            elif b[0][col]==opponent:
                return -10
    
    # checking for diagonl for x or o victory
    if b[0][0]==b[1][1] and b[1][1]==b[2][2]:
        if b[0][0]==player:
            return 10
        elif b[0][0]==opponent:
            return -10
    
    if b[0][2]==b[1][1] and b[1][1]==b[2][0]:
        if b[0][2]==player:
            return 10
        elif b[0][2]==opponent:
            return -10
    
    return 0

            


