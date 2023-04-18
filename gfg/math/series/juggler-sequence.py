"""
Juggler Sequence is a series of integer number in which the first
term starts with a positive integer number a and the remaining terms are
generated from the immediate previous term using the below recurrence relation
:
a(k+1)=

a(k+1)=a(k)pow(1/2) for even a(k)
a(k+1)=a(k)pow(3/2)
"""
import math 

def printJuggler(n):
    a=n
    # print the first term
    print(a,end=" ")
    # Calculate terms until last term is not 1
    while(a!=1):
        b=0
        # Check if previous term is even or odd 
        if(a%2==0):
            b=(int)(math.floor(math.sqrt(a)))
        else:
            # for odd previous term calculate next term
            b=(int)(math.floor(math.sqrt(a)*math.sqrt(a)*math.sqrt(a)))
        print(b,end=" ")
        a=b

"""
Important Points:

* The terms in Juggler Sequence first increase to a peak value
and then start decreasinng.

* The last term in Juggler Sequence is always 1.

"""
