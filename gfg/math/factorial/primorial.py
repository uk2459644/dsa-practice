"""
Given a number n, the task is to calculate its primorial.
Primorial (denoted as Pn#) is a product of first n prime numbers.
In primorial, not all the natural numbers get multiplied only prime
numbers are multiplied to calculate the primorial of a number.

A naive approach is to check all numbers from 1 to n one by one or not,
if yes then store the multiplication in result, similarly store the result
of multiplication of primes till n.

An efficient method is to find all the prime up to n
using Sieve of Sundaram and then just calculate the primorial by multiplying
them all.
"""
import math 

MAX=1000000

primes=[]

def sieveSundaram():
    marked=[False]*(int(MAX/2)+1)
    for i in range(1,int((math.sqrt(MAX)-1)/2)+1):
        for j in range(((i*(i+1))<<1),(int(MAX/2)+1),(2*i+1)):
            marked[j]=True
    
    primes.append(2)

    for i in range(1,int(MAX/2)):
        if (marked[i]==False):
            primes.append(2*i+1)
    
def calculatePrimorial(n):
    result=1
    for i in range(n):
        result=result*primes[i]
    
    return result


