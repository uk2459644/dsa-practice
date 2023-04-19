"""
IT is based on the fact that all primes greater than 3 are of the form
6k+1 or 6k-1, where k is any integer greater than 0. So, a more efficient
method is to test whether n is divisible by 2 or 3, then to check through
all numbers of the form 6k+-1 <= sqrt(n)

"""
import math 

def isPrime(n):
    if n==2 or n==3:
        return True 
    elif n<=1 or n%2==0 or n%3==0:
        return False 
    
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i == 0 or n%(i+2)==0:
            return False 
    
    return True

