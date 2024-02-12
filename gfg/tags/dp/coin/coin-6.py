"""
Coin change using the Top Down Memoization Dynamic Programming:

"""
import sys 

# Utility function for solving the minimum coinns problem

def minCoinsUtil(coins,m,V,dp):
    # Base case: If target value V is 0, no coins are needed
    if V==0:
        return 0
    
    # If subproblem is already solved, return the result
    if dp[V]!=-1:
        return dp[V]
    
    res=sys.maxsize 
    # Iterate over all coins and recursively solve for remaining value
    for i in range(m):
        if coins[i]<=V:
            # recursive call to solve for remaining value V
            sub_res=minCoinsUtil(coins,m,V-coins[i],dp)
            # If the subproblem has a valid solution and the total number of
            # coin is smaller than the current result, update the result
            if sub_res != sys.maxsize and sub_res+1 < res:
                res=sub_res+1 
    
    dp[V]=res

    return res
