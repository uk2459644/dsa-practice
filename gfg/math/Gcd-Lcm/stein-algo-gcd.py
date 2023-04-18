"""
Stein's algorithm or binary GCD algorithm is an algorithm that 
computes the greatest common divisor of two non-negative integers.
Stein's algorithm
replaces division with arithmetic shifts, comparisons
and substraction.

Algorithm '

if both a and b are 0, gcd is zero gcd(0,0)=0

gcd(a,0)=a and gcd(0,b)=b because everything divides 0.

if a and b are both even, gcd(a,b)=2*gcd(a/2,b/2)
because 2 is a common divisor. Multiplication with 2 can be done
with bitwise shift operator.

if a is even and b is odd, gcd(a,b)=gcd(a/2,b).
Similarly, if a is odd and b is even, then gcd(a,b)=gcd(a,b/2). It is 
because 2 is not a common divisor.

if both a and b are odd, then gcd(a,b)=gcd(|a-b|/2,b). Note that 
difference of two odd numbers is even

"""

def gcd(a,b):
    if (a==0):
        return b
    
    if(b==0):
        return a
    
    while (((a|b)&1)==0):
        a=a>>1
        b=b>>1
        k+=1 
    
    while((a&1)==0):
        a=a>>1 
    
    # from here on, 'a' is always odd.
    while (b!=0):
        # if b is even, remove all
        # factor of 2 in b
        while ((b&1)==0):
            b=b>>1
        
        if (a>b):
            temp=a
            a=b
            b=temp
        b=(b-a)
    return (a<<k)

