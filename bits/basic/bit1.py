# unsets the rightmost set bit of n 
# and return the result
import math

def fun(n):
    return n&(n-1)

# is power of four
def isPowerOfFour(n):
    return ((n&(n-1))==0) and ((32 + 1 - (math.floor(math.log(n)/math.log(2))))%2==1)

# code to check if given number is power of 
# 4 or not

def isPowerOfFour(n):
    return ((n>0) and ((n&(n-1))==0) and (n%3==1))


