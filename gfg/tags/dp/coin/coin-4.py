"""
Given a value V, if we want to make a change for V cents, and we have an 
infinity supply of each of C={C1,C2,..,Cm} valued coins, what is the minimum
number of coins to make  the change.If it's not possible to make a change,
print -1.

"""
# A Naive recursive python program to find minimum of coin 
# to make a given change V

import sys 

def minCoins(coins,m,V):
    # base case 
    if V==0:
        return 0
    # initialize result 
    res=sys.maxsize
    # Try every coin that has smaller value than V
    for i in range(0,m):
        if coins[i]<=V:
            sub_res=minCoins(coins,m,V-coins[i])
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if sub_res != sys.maxsize and sub_res+1<res:
                res=sub_res+1 
    
    return res


