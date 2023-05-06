"""
Given an integer N, the task is to check whether the
elements from the range [1,N] can be divided into three non empty equal sum
subsets.

Approach: There are two cases:

1. if N<=3: In this case, it is not possible to divide the elements in the 
   subsets that satisfy the given condition.

2. If N>3: In this case, it is only possible when the sum of all elements of the
   range [1,N] is divisible by 3 which can be easily calculated as 

   sum=(N*(N+1))/2. Now if sum%3==0 then print yes else print No
"""

def possible(n):
    if (n>3):
        sum=(n*(n+1))//2

        if (sum%3==0):
            return True
    
    return False

