"""
Divide array in two subsets such that sum of square of sum of both subsets is
maximum.

Approach: The task is to maximize the sum of a^2+b^2 where a and b are the sum
of the two subsets and a+b=c, i.e, the sum of entire array. The maximum sum 
can be achieved by sorting the array and dividing first N/2-1 smaller elements
in one subset and the rest N/2+1 elements in the other subset. In this way,
the sum can be maximized while keeping the difference in size at most 1.

"""

def maxSquareSubsetSum(A,N):
    sub1=0
    sub2=0

    A.sort()

    for i in range(N):
        if (i<(N//2)-1):
            sub1+=A[i]
        else:
            sub2+=A[i]
    
    return sub1*sub1 + sub2*sub2
