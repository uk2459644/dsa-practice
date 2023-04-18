"""
We find GCD of all possible subsets and find the largest subset
whose GCD is 1. Total time taken will be equal to the time taken
to evaluate GCD of all possible subsets are 2>n. In worst case there 
are n elements in subset and time taken to
calculate its GCD will be n*log(n) 


Optimized O(n) solution:
Let say we find a subset with GCD 1, if we add a new element to it 
then GCD will remains 1. Hence if a subset exists with GCD 1 then GCD of the
complete set is also 1. Hence we first find GCD of the GCD of the complete set,
if its 1 then complete set is that subset else no subset exist
with GCD 1.
"""

def gcd(a,b):
    if (a==0):
        return b
    
    return gcd(b%a,a)

# function to find largest subset with GCD 1

def largestGCDSubset(A,n):
    # finding gcd of whole array
    currentGCD = A[0]
    for i in range(1,n):
        currentGCD = gcd(currentGCD,A[i])
        if (currentGCD==1):
            return n
    return 0
