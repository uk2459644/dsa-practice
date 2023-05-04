"""
A Binomial coefficient C(n,k) can be defined as the coefficient of x^k
in the expansion of (1+x)^n.

A binomial coefficient C(n,k) also gives the number of ways, disregarding
order, that k objects can be chosen from among n objects more formally, the
number of k-element subsets (or k-combinations) of n-element set.

The Problem:
Write a function that takes two parameters n and k and returns the value
of Binomial Coefficient C(n,k).

1) Optimal Substructure
The value of C(n,k) can be recursively calculated using the following
standard formula for Binomial Coefficients.

C(n,k)=C(n-1,k-1)+C(n-1,k)
C(n,0)=C(n,n)=1
"""

def binomialCoeff(n,k):
    if k>n:
        return 0
    if k==0 or k==n:
        return 1
    
    return binomialCoeff(n-1,k-1)+binomialCoeff(n-1,k)

def binomailCoeff(n,k):
    C=[[0 for x in range(k+1)] for x in range(n+1)]
    # calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i,k)+1):
            # Base case
            if j==0 or j==1:
                C[i][j]=1
            # Calculate value using previously stored values
            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    
    return C[n][k]

"""
Space optimized version of the above code.
This one uses the concept of pascal Triangle and less memory.
"""
def binomialCoeff(n,k):
    # Declaring an empty array
    C=[0 for i in range(k+1)]
    # since nC0 is 1
    C[0]=1

    for i in range(1,n+1):
        # compute next row of pascal triangle using the 
        # previous row
        j=min(i,k)
        while (j>0):
            C[j]=C[j]+C[j-1]
            j-=1
    
    return C[k]



