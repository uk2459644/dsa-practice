"""
Optimized School Method: 

We cn do the following optimizations: Instead of checking till n, we can
check till sqrt(n) because a larger factor of n must be a multiple of a
smaller factor that has been already checked.

"""
import math 

def isPrime(n):
    if (n<=1):
        return False
    
    # check from 2 to sqrt(n)
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    
    return True

