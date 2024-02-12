"""
Efficient approach :

To optimize the above approach, the idea is to use Dynamic Programming. Two
possible options exist for every array element:
1. Either skip the current element and proceed to the next element.
2. Select the current element only if it is smaller than or equal to K.

Follow the steps below to solve the problem:
1. Initialize an array dp[N][K+1] with -1 where dp[i][j] will store the maximum
   sum to make sum j using elements up to index i.

2. From the above transition, find the maximum sums if the current elements gets 
   picked and if it is not picked, recursively.

3. Store the minimum answer for the current state. 

4. Also, add the base condition that if the current state (i,j) is already visited
   dp[i][j]!=-1 return dp[i][j].

5. Print dp[N][K] as the maximum possible sum.

"""

# Function to find the maximum sum that doesn't exceed K by choosing elements

def maxSum(a,n,k,dp):
    # Base case
    if n<=0:
        return 0
    
    # Return the memoized state
    if dp[n][k]!=-1:
        return dp[n][k]
    
    # Don't pick the current element
    option=maxSum(a,n-1,k,dp)

    # Pick the current element
    if (k>=a[n-1]):
        option=max(option,a[n-1]+maxSum(a,n-2,k-a[n-1],dp))

    dp[n][k]=option

    # return and store the result
    return dp[n][k]

if __name__=="__main__":
    arr=[50,10,20,30,40]
    N=len(arr)
    K=100

    # Initialize dp
    dp=[[-1 for i in range(K+1)] for j in range(N+1)]

    print(maxSum(arr,N,K,dp))
    print(dp)


