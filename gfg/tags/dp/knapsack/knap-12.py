"""
Let' look at the recurrence relation firt. This method is valid
for all the integers.

dp[i][C]=dp[i-1][C-arr[i]]+dp[i-1][C]

Let's understand the state of the DP now. Here, dp[i][C] stores the number
of subsets of the sub-array arr[i...N-1] such that their sum is equal to C.

Thus, the recurrence is very trivial as there are only two choices, either
consider the ith element in the subset or don't.

"""

def subset_sum(a:list,n:int,sum:int):
    # initializing  the matrix
    tab=[[0]*(sum+1) for i in range(n+1)]

    tab[0][0]=1
    for i in range(1,sum+1):
        tab[0][i]=0
    
    for i in range(1,n+1):
        for j in range(sum+1):
            if a[i-1]<=j:
                tab[i][j]=tab[i-1][j]+tab[i-1][j-a[i-1]]
            else:
                tab[i][j]=tab[i-1][j]
    
    return tab[n][sum]

"""
Method 3: Space Optimization

We can solve this problem by just taking care of last state and current state
so we can wrap up this problem in O(target +1) space complexity.

"""


