"""
Given an integer array of coins[] of size N representing different types
of currency and an integer sum, The task is to find the number of ways to make sum
by using different combinations from coins[].

"""

# REcursive program for coin change problem

def count(coins,n,sum):
    # if sum is 0 then there is 1 solution 
    # do not include any coin
    if (sum==0):
        return 1
    # if sum is less than 0 then no solution exists
    if sum<0:
        return 0
    # if there are no coins and um is greater than 0, then no
    # solution exist
    if n<=0:
        return 0
    
    # count is sum of solutions (i) including coins[n-1] excluding coins[n-1]
    return count(coins,n-1,sum)+count(coins,n,sum-coins[n-1])

