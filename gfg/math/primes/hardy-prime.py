"""
Hardy Ramanujam theorem states that the number of prime
factors of n will approximately be log(log(n)) for most
natural numbers n.

"""
import math 

def exactPrimeFactorCount(n):
    count=0
    if (n%2==0):
        count+=1 
        while (n%2==0):
            n=int(n/2)
    i=3
    while (i<=int(math.sqrt(n))):
        if (n%i==0):
            count+=1 
            while (n%i==0):
                n=int(n/i)
        i+=2 
    
    if (n>2):
        count+=1 
    return count



