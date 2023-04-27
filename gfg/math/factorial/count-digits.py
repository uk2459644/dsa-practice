"""
A naive solution would be to calculate the n! first and then
calculate the number of digits present in it. 

We know,
log(a*b)=log(a)+log(b)

Therefore
log(n!)=log(1*2*3...*n)=log(1)+log(2)+...+log(n)

Now, observe that the floor value of log base 10 increased by 1,
of any number, gives the number of digits present in that number.

ans=floor(log(n!))+1
"""
import math

def findDigits(n):
    if n<0:
        return 0
    
    if n<=1:
        return 1
    
    digits=0
    for i in range(2,n+1):
        digits+=math.log10(i)
    
    return math.floor(digits)+1

