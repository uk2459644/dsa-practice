# A dynamic programming based program to find minimum
# number of squares whose sum is equal to a given number

from math import ceil, sqrt

# returns count of minimum squares that sum to n

def getMinSquares(n):
    # Create a dynamic programming table to  store sq and getMinSquares
    # table for base entries
    dp=[0,1,2,3]
    # getMinsquares rest of the table using recursive formula
    for i in range(4,n+1):
        # max value is i as i can always
        # be represented as 1*1+1*1+...

        dp.append(i)

        # Go through all smaller numbers to recursively find minimum
        for x in range(1,int(ceil(sqrt(i)))+1):
            temp=x*x
            if temp>i:
                break
            else:
                dp[i]=min(dp[i],1+dp[i-temp])

    # store result
    return dp[n]


