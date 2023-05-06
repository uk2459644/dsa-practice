"""
Given a number n, print all primes smaller than n.

A Naive approach is to run a loop from 0 to n-1 and check number for 
primeness.

"""
def simpleSieve(limit):
    # create a boolean array and initialize all entries of it as true.
    # A value in mark[p] will finally be false if 'p' is not a prime, 
    # true.
    mark=[True for i in range(limit)]

    # one by one traverse all numbers so that their
    # multiples can be marked as composite.
    for p in range(p*p,limit-1,1):
        # if p is not changed, then it is a prime
        if (mark[p]==True):
            for i in range(p*p,limit-1,p):
                mark[i]=False
    
    for p in range(2,limit-1,1):
        if (mark[p]==True):
            print(p,end=" ")
            
