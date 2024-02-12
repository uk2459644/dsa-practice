"""
Given a value V, if we want to make a change for V cents, and we have an
infinite supply of each of C={c1,c2,..,c} valued coins, what is the 
minimum number of coins to make the change? If it's not possible to make a change,
print -1.

"""

"""
Approach 1: 
IF V==0, then 0 coins required.
if v>0:
   minCoints(coins[0..m-1],V)=min{1+minCoins(V-coin[i])}

"""
import sys 

# m is size of coins array (number of different coins)
def minCoins(coins,m,V):
    # base case 
    if(V==0):
        return 0
    # Initialize result
    res=sys.maxsize
    # try every coin that has smaller value than V
    for i in range(0,m):
        if (coins[i]<=V):
            sub_res=minCoins(coins,m,V-coins[i])
            # check for INT_MAX to avoid overflow and see if result can
            # minimized
            if (sub_res != sys.maxsize and sub_res+1 < res):
                res=sub_res+1
    
    return res

"""
Approach 2:
DP
"""

def minCoins(coins,m,V):
    # table[i] will be storing the minimum number of coins required for i
    # value So table[V] will have result
    table=[0 for i in range(V+1)]
    # Base case if given value is 0
    table[0]=0
    # Initialize all table value as infinite
    for i in range(1,V+1):
        table[i]=sys.maxsize
    
    # Compute minimum coins required for all values from 1 to v
    for i in range(1,V+1):
        # Go through all coins smaller than i
        for j in range(m):
            if coins[j]<=i:
                sub_res=table[i-coins[j]]
                if (sub_res != sys.maxsize and sub_res+1 < table[i]):
                    table[i]=sub_res+1
    
    if table[V]==sys.maxsize:
        return -1
    return table[V]


