"""
Given two numbers n and k, print
k-th prime factor among all prime factors of n.
"""
import math 

def kPrimeFactor(n,k):
    while (n%2==0):
        k-=1 
        n=n//2
        if (k==0):
            return 2 
        
    i=3
    while i<= math.sqrt(n):
        while (n%i==0):
            if (k==1):
                return i
            k=k-1
            n//=i
        i+=2
    if (n>2 and k==1):
        return n
    return -1 


