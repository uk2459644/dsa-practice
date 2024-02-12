
# Calculate the maximum score possible for p1 if only the bags from
# beg to end were available

def maxScore(money,beg,ed):
    # Length of the game
    totalTurns=len(money)

    # which turnn is being played
    turnsTillNow=beg+((totalTurns-1)-ed)
    # base case
    if (beg==ed):
        # If it is P1's turn
        


