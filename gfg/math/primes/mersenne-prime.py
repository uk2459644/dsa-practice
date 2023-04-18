"""
Mersennse Prime is a prime number that is one
less than a power of two. In other words, any prime is Mersenne
Prime if it is of the form 2^k-1 where k is an integer greater than
or equal to 2. 

First few Mersenne Primes are 3,7,31 and 127.
"""

def SieveOfEratosthenes(n,prime):
    for i in range(0,n+1):
        prime[i]=True 
    
    p=2
    while (p*p<=n):
        if (prime[p]==True):
            for i in range(p*2, n+1,p):
                prime[i]=False 
        p+=1 

def mersennePrimes(n):
    prime=[0]*(n+1)
    SieveOfEratosthenes(n,prime)
    k=2 

    while(((1<<k)-1)<=n):
        num=(1<<k)-1 

        if (prime[num]):
            print(num, end=" ")
        k+=1 
        