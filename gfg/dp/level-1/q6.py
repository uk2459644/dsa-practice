import sys

# m is size of array of coins (number of different coins)
def minCoins(coins,m,V):
    # base case
    if V==0:
        return 0
    
    # Initialize result
    res=sys.maxsize

    # Try every coin that has smaller value than V
    for i in range(0,m):
        if (coins[i]<=V):
            sub_res=minCoins(coins,m,V-coins)

            # Check for INT_MAX to avoid overflow and see if result
            # can minimized
            if (sub_res != sys.maxsize and sub_res+1<res):
                res=sub_res+1
    
    return res
