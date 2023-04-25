"""
Given three integers a,b,n. Your task is to print numbers between a and b including
them also which have n-divisors. A number is called n-divisor if it has total n
divisor including 1 and itself.
"""
import math 

def sieve(primes,x):
    primes[1]=False
    # if a number is prime mark all its multiple as non prime
    i=2
    while (i*i<=x):
        if primes[i]==True:
            j=2
            while (j*i<=x):
                primes[i*j]=False
                j+=1
        i+=1

def nDivisors(primes,x,a,b,n):
    result=0
    v=[]
    for i in range(2,x+1):
        if (primes[i]):
            v.append(i)
    
    for i in range(a,b+1):
        temp=i
        total=1
        j=0
        k=v[j]
        while (k*k<=temp):
            count=0
            while (temp%k==0):
                count+=1 
                temp=int(temp/k)
            
            total=total*(count+1)
            j+=1 
            k=v[j]
        
        if(temp!=1):
            total=total*2
        
        if (total==n):
            result+=1
    
    return result
