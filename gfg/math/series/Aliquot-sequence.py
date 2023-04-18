"""
Aliquot sequence of a number starts with itself, remaining terms of 
the sequence are sum of proper divisors of immediate previous term.

Important Points: 

Numbers which have repeating Aliquot sequence of length 1 are called
Perfect Numbers. For example 6, sum of its proper divisors is 6

Numbers which have repeatinng Aliquot sequence of length 2 are called 
Amicable Number.

Numbers which have repeating Aliquot sequence of length 3 are called sociable number.

It is conjectured that every aliquot sequence ends in one of the following ways.

- with a prime number which in turn ends with 1 and then 0.
- a perfect number
- a set of amicable or sociable numbers.

"""
from math import sqrt 

def getSum(n):
    summ=0

    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            if n//i==i:
                summ+=i 
            else:
                summ+=i 
                summ+=n//i 
    
    return summ-n

