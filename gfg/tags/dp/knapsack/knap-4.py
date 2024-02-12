"""
Given an integer array W[] consisting of weights of the items and some queries
consisting of capacity C of knapsack, for each query find maximum weight we can
put in the knapsack. Value C doesn't exceed a certain integer C_MAX.

"""

"""
Naive Approach: For each query, we can generate all possible subsets of weight and
choose the one that has maximum weight among all those subsets that fits in
the knapsack. 

Efficient approach: We will optimize answering each query using dynamic programming.
0-1 knapsack is solved using 2-d dp, one state 'i' for current index (select or reject)
and one for remaining capacity 'R'.

"""

import numpy as np
import sys

C_MAX=30
max_arr_len=10

# to store state of dp
dp=np.zeros((max_arr_len,C_MAX+1))

# to check if a state has been solved
v=np.zeros((max_arr_len,C_MAX+1))

INT_MIN=-(sys.maxsize)+1 

# function to compute the states
def findMax(i,r,w,n):
    # base case
    if (r<0):
        return INT_MIN
    if i==n:
        return 0
    
    # check if a state has been solved 
    if v[i][r]:
        return dp[i][r]
    
    # Setting a state as solved
    v[i][r]=1
    dp[i][r]=max(w[i]+findMax(i+1,r-w[i],w,n),findMax((i+1,r,w,n)))

    return dp[i][r]

# Function to precompute the states
def preCompute(w,n):
    for i in range(C_MAX,-1,-1):
        findMax(0,i,w,n)

# function to answer a query in O(1)
def ansQuery(w):
    return dp[0][w]




