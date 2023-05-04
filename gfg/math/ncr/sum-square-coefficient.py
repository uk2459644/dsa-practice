"""
Given a positive integer n. The task is to find the sum of square of 
Binomial Coefficient...

Method 1: 
The idea is to generate all the terms of binomial coefficient and find the
sum of square of each binomial coefficient.

"""

def sumofsquare(n):
    C=[[0 for i in range(n+1)] for j in range(n+1)]
    # calculate the value of Binomial Coefficient in bottom up manner

    for i in range(0,n+1):
        for j in range(0,min(i,n)+1):
            # base case
            if (j==0 or j==1):
                C[i][j]=1
            # calculate value using previously stored values
            else:
                C[i][j]=(C[i-1][j-1]+C[i-1][j])
    
    # finding the sum of square of binomial coefficient
    sum=0
    for i in range(0,n+1):
        sum=sum+(C[n][i]*C[n][i])
    
    return sum

"""
Method 2: Using Formula 

2nCn=(2n!)/(n!)^2

"""
def factorial(start,end):
    res=1

    for i in range(start,end+1):
        res*=i
    
    return res

def sunofsquare(n):

    return int(factorial(n+1,2*n)/factorial(1,n))

