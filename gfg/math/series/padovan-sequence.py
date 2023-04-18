"""
Padovan Sequence:

Similar to Fibonacci sequene with similar recursive structure. The recursive
formula is,

P(n)=P(n-2)+P(n-3)
P(0)=P(1)=P(2)=1

"""

# Python program to find n'th term is padovan sequece
# using dynamic programming

def pad(n):
    pPrevPrev, pPrev, pCurr, pNext = 1,1,1,1

    for i in range(3,n+1):
        pNext=pPrevPrev+pPrev
        pPrevPrev=pPrev
        pPrev=pCurr
        pCurr=pNext
    
    return pNext
