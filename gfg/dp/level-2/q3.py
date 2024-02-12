
# Subset sum problem using Dynamic Programming

# So we will create a 2D array of size (n+1)*(sum+1) of type boolean.
# The state dp[i][j] will be true if there exists a subset of elements
# from set[0...i] with sum value='j'

# The dynamic programming relation is as follows
# if (A[i-1]>j):
#     dp[i][j]=dp[i-1][j]
# else:
#    dp[i][j]=dp[i-1][j] OR dp[i-1][j-set[i-1]]

def isSubsetSum(set,n,sum):
    # The value of subset[i][j] will be true if there is a
    # subset[0..j-1] with sum equal to i
    subset=[[False for i in range(sum+1)] for i in range(n+1)]
    # if sum is 0, then answer is true
    for i in range(n+1):
        subset[i][0]=True

    # If sum is not 0 and set is empty, then answer is false
    for i in range(1,sum+1):
        subset[0][i]=False
    
    # Fill the subset table in bottom up manner
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<set[i-1]:
                subset[i][j]=subset[i-1][j]
            
            if j>=set[i-1]:
                subset[i][j]=(subset[i-1][j] or subset[i-1][j-set[i-1]])
    
    return subset[n][sum]


