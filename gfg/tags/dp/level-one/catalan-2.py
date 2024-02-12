"""
Dynamic programming solution for catalan number:

We can observe that the above recursive implementation does a lot of
repeated work. Since there are overlapping subproblems, we can use
dynamic programming for this.

Below is the implementation of the above idea: 
- Create an array catalan[] for storing ith catalan number.
-Initialize, catalan[0] and catalan[1]=1
-Loop through j=0 to j<i and keep adding value of catalan[j]*catalan[i-j-1]
 into catalan[i].

Finally, return catalan[n]

"""

# A dynamic programming based function to find nth catalan number

def catalan(n):
    if n==0 or n==1:
        return 1
    # Table to store results of subproblems
    catalan=[0]*(n+1)
    # Initialize first two values in table
    catalan[0]=1
    catalan[1]=1
    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2,n+1):
        for j in range(i):
            catalan[i]+=catalan[j]*catalan[i-j-1]
    
    # return last entry
    return catalan[n]



