"""
Key Concept: Our idea is to store the smallest prime factor for every number.
Then to calculate the prime factorization of the given number by dividing the
given number repeatedly with its smallest prime factor till it becomes 1.

Now, after we are done with precalculating the smallest prime factor for every
number we will divide our number n by its corresponding smallest prime 
factor till n becomes 1.
"""
import math as mt 

MAXN=100001

spf =[0 for i in range(MAXN)]

def sieve():
    spf[1]=1 
    for i in range(2,MAXN):
        spf[i]=i 
    
    for i in range(4,MAXN,2):
        spf[i]=2 
    
    
    for i in range(3,mt.ceil(mt.sqrt(MAXN))):
        if (spf[i]==i):
            for j in range(i*i,MAXN,i):
                if (spf[j]==j):
                    spf[j]=i 

def getFactorization(x):
    ret=list()
    while (x!=1):
        ret.append(spf[x])
        x=x//spf[x]
    
    return ret

