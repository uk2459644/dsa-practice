import sys 

# function to count the maximum score of an
# index 

def maxScore(i,A,K,N,dp):
    # base case 
    if i>=N-1:
        return A[N-1]
    
    # If the value for the current index is 
    # pre-calculated 

    if dp[i]!=-1:
        return dp[i]
    
    score = 1- sys.maxsize

    # Calculate maximum score for all the steps
    for j in range(1,K+1):
        score=max(score,maxScore(i+j,A,K,N,dp))
    
    dp[i]=score+A[i]

    return dp[i]

def getScore(A,N,K):
    dp=[0]*N
    maxScore(0,A,K,N,dp)
