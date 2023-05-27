"""
Validity of a given Tic-Tac-Toe board configuration

A Tic Tac Toe board is given after some moves are played. Find out if the
given board is valid, is it possible to reach this board position after some moves or not.

Basically, to find the validity of an input grid, we can think of the
conditions when an input grid is invalid. Let no. of "X"s be countX and another
counntO. Since we know that the game starts with X, a given grid of Tic-Tac-Toe game would be definitely invalid if 
following two conditions meet

1. countX != countO and
2. countX != countO+1 

- Since X is always the first move, second condition is also required.
- Now does it mean that all the remaining board positions are valid one? The answer
  NO. Think of the cases when input grid is such that both X and O are making
  straight lines. This is also not.

- Valid position because the game ends when one player wins, So we need to check
  the following condition as well.

"""
def win_check(arr,char):
    # check all possible winning combinations
    matches=[[0,1,2],[3,4,5],
             [6,7,8],[0,3,6],
             [1,4,7],[2,5,8],
             [0,4,8],[2,4,6]]
    
    for i in range(8):
        if (arr[(matches[i][0])]==char and 
            arr[(matches[i][1])]== char and
            arr[(matches[i][2])]== char):
            return True
    
    return False

def is_valid(arr):
    # count number of 'X' and 'O' in the given board
    xcount=arr.count('X')
    ocount=arr.count('O')
    # Board can be valid only if either xcount and ocount is same or count
    # is one more than ocount
    if (xcount == ocount+1 or xcount==ocount):
        # check if O wins 
        if win_check(arr,'O'):
            # check if x wins, at a given point only on
            # if x also wins then return invalid
            if win_check(arr,'X'):
                return "InValid"
            # O can only win if xcount == ocount
            if xcount == ocount:
                return "Valid"
        
        if win_check(arr,"X") and xcount != ocount+1:
            return "InValid"
        
        # if o is not the winner return valid
        if not win_check(arr,'O'):
            return "Valid"
    
    # If nothing above matches return invalid
    return "Invalid"

