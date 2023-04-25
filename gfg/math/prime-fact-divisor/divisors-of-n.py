"""
A naive solution would be to iterate all the numbers from 1 to n, checking if that
number divides n and printing it.
"""
import math

def printDivisors(n):
    i=1
    while i<=n:
        if (n%i==0):
            print(i,end=" ")
        i+=1

def printDivisors(n):
    i=1
    while i<=math.sqrt(n):
        if (n%i==0):
            if (n/i==i):
                print(i)
            else:
                print(i,int(n/i))
        i+=1 
        

