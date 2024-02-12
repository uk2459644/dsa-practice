"""
Find the longest common subsequence LCS in given K permutations

Approach: 
This problem is an extension of longest common subsequence. The solution is based on the concept
of dynamic programming. Follow the steps below:

- Create a 2D array(pos[][]) to store position of all the numbers from 1
  to N in each sequence, where pos[i][j] denotes position of value j in ith 
  sequence.

- Initialize an array(dp[]) where dp[i] stores the longest common subsequence
  ending at position i.
   - Consider the first sequence as reference and for each element of the first
   sequence
  
"""

# Function to find the longest common sub-sequence of k permutation
def findLcs(arr,n,k):
    # Variable to keep track of the length of the longest common sub-sequence
    maxlen=0
    # position array to keep track of position of elements in each permutation
    pos=[0]*k 
    for i in range(len(pos)):
        pos[i]=[0]*n
    
    dp=[0]*n 
    for i in range(k):
        for j in range(n):
            pos[i][arr[i][j]-1]=j
    
    # Loop to calculate the LCS of all the permutations 
    for i in range(n):
        dp[i]=1 
        for j in range(i):
            good=True
            

