"""
Python program to print prime factors 

"""

import math 

def primeFactors(n):
    # print the number of two's that divide n
    while n%2==0:
        print(2)
        n=n/2 
    # n must be odd at this point 
    # so a skip of two cn be used
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            print(i)
            n=n/i 
    
    if n>2:
        print(n)
        
