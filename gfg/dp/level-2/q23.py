# Recursive memoization function to count the number of distinct 
# ways to make the sum by using n coins

def count(coins,sum,n,dp):
    # base case
    if sum==0:
        dp[n][sum]=1
        return dp[n][sum]
    
    # if number of coins is 0 or sum is less than 0 then
    if n==0 or sum<0:
        return 0
    
    # if the subproblem is previously calculated then
    if dp[n][sum]!=-1:
        return dp[n][sum]
    
    # two options for the current coin
    dp[n][sum]=count(coins,sum-coins[n-1],n,dp)+count(coins,sum,n-1,dp)

    return dp[n][sum]

