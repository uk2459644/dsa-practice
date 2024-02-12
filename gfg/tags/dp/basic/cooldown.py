"""
Given the prices of stock for n number of days. Every ith
day tell the price of the stock on that day. Find the maximum profit that
you can make by buying and selling stock with the restriction of after you sell 
you can not buy stock on the next day.

"""
"""
Approach: 


We need to maintain three states for each day. The first stage will be
maxed profit we can make if we have one stock yet to be sold. The second
stage will have the max profit we can make if we have no stock left to be sold.
The third state is the cooldown state.

"""

# Python program to maximize profit by buying and selling stock with cooldown

def maximumProfit(v):
    n=len(v)
    dp=[[0,0,0] for _ in range(n+1)]

    for i in range(1,n+1):
        # Maximum of buy state profit till the previous day or
        # buying a new stock with the cooldown state of the previous day

        dp[i][0]=max(dp[i-1][0],dp[i-1][2]-v[i-1])

        # Maximum of sold state profit till the previous day or selling
        # the stock on the current day with buy state of the previous day
        dp[i][1]=max(dp[i-1][1],dp[i-1][0]+v[i-1])

        # sold state of the previous day
        dp[i][2]=dp[i-1][1]

    return dp[n][1]



