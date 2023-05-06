"""
Python program for the above approach
"""
Primes=[0]*500001

def SieveOfEratosthenes(n):
    Primes[0]=1
    i=3
    while (i*i<=n):
        if (Primes[i//2]==0):
            for j in range(3*i,n+1,2*i):
                Primes[j//2]=1
        i+=2
        
