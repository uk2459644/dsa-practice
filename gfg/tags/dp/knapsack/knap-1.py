"""
0/1 Knapsack Problem :

We are given N items where each item has some weight and profit associated with
it. We are also given a bag with capacity W, [ the bag can hold at most W weight in it].
The target is to put the items into the bag such that the sum of profits associated
with them is the maximum possible.

"""

"""
Recursion Approach for 0/1 Knapsack problem:

To solve the problem follow the below idea:

A simple solution is to consider all subsets of items and calculate the total
weight and profit of all subsets. Consider the only subset whose total weight
is smaller than W. From all such subsets, pick the subset with maximum profit.

Optimal Substructure: To consider all subsets of items, there can be two cases
for every items.

Case 1: The item is included in the optimal subset.

Case 2: The item is not included in the optimal set.

"""

"""
Follow the below steps to solve the problem: 

The maximum value obtained from 'N' items and W weight excluding ntth item)

- Maximum value obtained by N-1 items and W weight (excluding nth item).
- Value of nth item plus maximum value obtained by N-1 items and (W-weight of the Nth item)
  
"""

# Returns the maximum value that can be put in a knapsack of capacity W

def knapSack(W,wt,val,n):
    # Base case 
    if n==0 or W==0:
        return 0
    
    # If weight of the nth item is more than Knapsack of capacity W, then
    # this item cannot be included in the optimal solution

    if (wt[n-1]>W):
        return knapSack(W,wt,val,n-1)
    
    # return the maximum of two cases: 1. nth item included 2. not included
    else:
        return max(val[n-1]+knapSack(W-wt[n-1],wt,val,n-1),knapSack(W,wt,val,n-1))

# Dynamic Programming Approach for 0/1 Knapsack Problem:
"""
Memoization Approach for 0/1 knapsack problem using dynamic programming:

If we get a subproblem the first time, we can solve this problem by creating a
2-D array that can store a particular state (n,w). Now if we come across the same 
state (n,w) again instead of calculating it in exponential complexity we can directly
return its result stored inthe table in canstant time.

"""

# This is the memoization approach of 0/1 knapsack

def knapSack(wt,val,W,n):
    # base condition
    if n==0 or W==0:
        return 0
    
    if t[n][W]!=-1:
        return t[n][W]
    
    # choice diagram code 
    if wt[n-1]<=W:
        t[n][W]=max(val[n-1]+knapSack(wt,val,W-wt[n-1],n-1),knapSack(wt,val,W,n-1))

        return t[n][W]
    
    elif wt[n-1]>W:
        t[n][W]=knapSack(wt,val,W,n-1)
        return t[n][W]
    

# Overlapping Sub-problem property approach for 0/1 knapsack problem using
# dynamic programming

"""
Since subproblem are evaluated again, this problem has Overlapping sub-problem
property So the 0/1 knapsack problem has both properties.

Follow the below steps to solve the problem:

-Consider the same cases as mentioned in the recursive approach.
- In a DP[][] table let's conider all the possible weights from 1 to W
  as the columns and the element that can be kept as rows.
- The state DP[i][j] will denote the maximum value of j-weight considering all 
  values from 1 to ith. So if we consider wi weight in ith row we can fill it in 
  all columns which have weight values>wi. Now two possibilities can take place:
  - Fill wi in the givenn column.
  - Do not fill wi in the given column.

- Now we have to take a maximum of these two possiblities, 
  - Formally if we do not fill the ith weight in the jth column then the 
    DP[i][j]

"""

def knapSack(W,wt,val,n):
    K=[[0 for x in range(W+1)] for x in range(n+1)]

    # Build table k[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]

    
    return K[n][W]

"""
Space optimized Approach for 0/1 knapsack problem using Dynamic programming :

For calculating the current row of the dp[] array we require only previous row,
but if we start traversinng the rows from right to left then it can be done with 
a single row only.

"""

def knapSack(W,wt,val,n):
    dp=[0 for i in range(W+1)]

    for i in range(1,n+1):
        # Starting from back, so that we also have data of previous computation
        # when taking i-1 items
        for w in range(W,0,-1):
            if wt[i-1]<=w:
                # finding the maximum value 
                dp[w]=max(dp[w],dp[w-wt[i-1]]+val[i-1])
        
        # return the maximum value of knapsack
        return dp[W]
    

