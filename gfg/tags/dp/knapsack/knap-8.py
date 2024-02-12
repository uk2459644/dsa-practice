"""
Given an integer W, arrays val[] and wt[], where val[i] and wt[i]
are the values and weights of the ith item, the tassk i to 
calculate the maximum value that can be obtained using weights not
exceeding W.

"""
"""
Efficient Approach: The above approach can be optimized based on the 
following observations: 

- Suppose the ith index gives us the maximum value per unit weight in the given data
  which can be easily found in O(n).

- For any weight X, greater than or equal to wt[i], the maximum reachable value
  dp[X-wt[i]]+val[i]
"""
from fractions import Fraction 

# function to implement optimized unbounded knapsack algorithm

def unboundKnapsackBetter(W,val,wt):
    # stores most dense item
    maxDenseIndex=0
    # find the item with highest unit value then chooe
    for i in range(1,len(val)):
        if Fraction(val[i],wt[i])

