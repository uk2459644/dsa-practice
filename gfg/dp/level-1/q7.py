# A Dynamic programming based problem to find minimum of coins to make
# a given change V

import sys

def minCoins(coins,m,V):
    # table[i] will be storing the minimum number of coins required for i
    # value, So table[v] will have result
    table=[0 for i in range(V+1)]
    # Base case (if given value V is 0)
    table[0]=0

    # Initialize all table value as infinite
    for i in range(1,V+1):
        table[i]=sys.maxsize
    
    # compute minimum coins required
    # for all values from 1 to V
    for i in range(1,V+1):
        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j]<=i):
                sub_res=table[i-coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1< table[i]):
                    table[i]=sub_res+1
    
    if table[V]==sys.maxsize:
        return -1
    
    return table[V]



