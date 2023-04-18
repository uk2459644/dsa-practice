"""
In mathmatics, Rosser's Theorem states that the nth prime
number is greater than the product of n and naturl logarithm of n for all
n greater than 1.

Mathematically,
for n>=1, if p is the nth prime number, then p>n*log(n)

"""
import math 

prime = []

def sieve():
    n=100001
    isprime = [True]*(n+2)
    isprime[0]=False 
    isprime[1]=False 
    for i in range(2,n+1):
        if (isprime[i]):
            j=i*i 
            while (j<=n):
                isprime[j]=False 
                j+=i 
    
    for i in range(n+1):
        if (isprime[i]):
            prime.append(i)

def verifyRosser(n):
    for i in range(n):
        if (prime[i]>int((i+1)*math.log(i+1))):
            print(prime[i])
