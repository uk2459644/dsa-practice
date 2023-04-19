"""
School Method: 

A simple solution is to iterate through all numbers from 2 to n-1 
and for every number check if it divides n. If we find any number that
divides, we return false.

"""
def isPrime(n):
    if n<=1:
        return False 
    
    # check from 2 to n-1 
    for i in range(2,n):
        if n%i==0:
            return False 
    
    return True 



