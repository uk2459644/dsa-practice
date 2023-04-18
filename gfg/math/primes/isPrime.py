"""
Iterate through all numbers from 2 to ssquare root of n and for every
number check if it divides n [because if a number is expressed as n=xy
 and any of the x or y is greater than the root of n, the other must be less than
 the root value]. If we find any number that dividdes, we return false.

"""

from math import sqrt

# Function check whether a number is 
# prime or not

def isPrime(n):
    if (n<=1):
        return False 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n%i==0):
            return False 
    
    return True 
