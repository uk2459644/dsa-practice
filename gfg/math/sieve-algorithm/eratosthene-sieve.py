"""
Given a number n, print all primes smaller than or equal to n. It is
also given that n is a small number.

"""

def SieveOfEratosthenes(n):
    # Create a boolean array prime[0...n] and initialize all
    # entries it as true. A value in prime[i] will finally be false if
    # i is not a prime, else true.

    prime=[True for i in range(n+1)]
    p=2

    while (p*p<=n):
        # if prime[p] is not changed, then it is a prime
        if (prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1 
    
    for p in range(2,n+1):
        if prime[p]:
            print(p)
            
