"""
Second Approach: This approach is similar to Sieve of Eratosthenes

We can achieve O(logn) for all composite numbers by consecutive dividing of the
given number by an integer starting from 2 representing current factor of
that number. This approach works on the fact that all composite numbers have
factors inpairs other than 1 or number itself.

Therefore if we start dividing the number by the smallest possible prime 
number (2) then all of its multiples or numbers will automatically be removed
before we actually reach that number.

"""

def primeFactors(n):
    c=2
    while(n>1):
        if(n%c==0):
            print(c,end=" ")
            n=n/c 
        else:
            c+=1 
            