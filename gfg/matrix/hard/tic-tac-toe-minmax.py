"""
Evaluation function for Tic Tac Toe board.

"""
def evaluate(b):
    # checking for rows for x or 0 victory
    for row in range(0,3):
        if b[row][0]==b[row][1] and b[row][1]==b[row][2]:
            if b[row][0]=='x':
                return 10
        elif b[row][0] == 'o':
            return -10
    
    # checking for columns for x or 0 victory
    for col in range(0,3):
        if b[0][col]==b[1][col] and b[1][col] == b[2][col]:
            if b[0][col]=="x":
                return 10
            elif b[0][col]=="o":
                return -10
    
    # checking for diagonals for x or o victory
    if b[0][0]==b[1][1] and b[1][1]==b[2][2]:
        if b[0][0]=="x":
            return 10
        elif b[0][0]=="o":
            return -10
    
    if b[0][2]==b[1][1] and b[1][1]==b[2][0]:
        if b[0][2]=='x':
            return 10
        elif b[0][2]=="o":
            return -10
    
    return 0




