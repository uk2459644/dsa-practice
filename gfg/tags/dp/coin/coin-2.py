"""
Coin change by using Dynamic Programming: Bottom Up Memoization

Algorithm : 
The coin change problem is a clasic dynamic programming problem that involves
finding the number of ways to make change for a given amount of money using a 
given set of coins. Here's a step by step solution for the coin change problem: 

Define the problem: Given a target amount and a set of coin denominations, find
the total number of unique ways to make change for the target amount using the coins.

Identify the subproblem: We can break the problem down into subproblems by 
considering the subproblem of making change for smaller amounts firs. For each coin
denomination, we can ask how many ways there are to make change for the remaining amount 
after subtracting the coin value.

Define the base cases: If the target aount is zero, there is exactly one way to make change
(using no coins). If the target amount is negative, there are no ways to make change for the amount.

Define the recursive formula: Let dp[i] be the number of ways to make change for the amount i.
Then we can calculate dp[i] for all i using the formula:

dp[i]=sum(dp[i-coin]) for coin in coins 

This means that the number of ways to make change for i is the sum of the 

"""

# Dynamic programming implementation of coin change problem

def count(coins,n,sum):
    # WE need sum+1 rows as the table is counstructed in bottom up manner using
    # the base case 0 value case sum=0
    table=[[0 for x in range(n)] for x in range(sum+1)]
    # Fill the entries for 0 value case n=0
    for i in range(n):
        table[0][i]=1

    # Fill the rest of the table entries in bottom up manner
    for i in range(1,sum+1):
        for j in range(n):
            # count of solution including coins[j]
            x=table[i-coins[j]][j] if i-coins[j]>=0 else 0
            # count of solutions excluding coins[j]
            y=table[i][j-1] if j>=1 else 0 
            # total count 
            table[i][j]=x+y
    
    return table[sum][n-1]

