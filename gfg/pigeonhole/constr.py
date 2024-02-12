"""
Construct a string that contains a times letter 'A' and b times
letter 'B' (a>b) such that maximum continuous occurence of a letter
is as small as possible.
"""
"""
Approach: 

Since a>b, it can be easily observed that 'B' is dividing the whole string
in (b+1) parts.
According to the pigeonhole principle, at least one region must have
at least p=[a/(b+1)] A's. First, place p number of 'A' in every (b+1) region.
Now remaining 'A's can be equally distributed in the regions.
"""

def generateans(a,b):
    temp=b+1
    s=""
    # run a loop until b is greater than 0
    while temp>0:
        each = (a//(b+1))

        while each > 0:
            s+='A'
            a-=1 
            each -=1 
        
        if (b>0):
            s+='B'
            b-=1 
        temp -= 1

    return s 
        
"""
Another approach: 

We can start by appending 'AB' pairs until we are left with only 'a-b'
'A' characters. Then, we can append remaining 'A' characters at the end.
This will give us the desired string with minimum consecutive occurence.
"""
def generateans(a,b):
    s=""
    countA, countB = a, b
    appendA = True
    while countA > 0 or countB > 0:
        if appendA:
            s+= 'A'
            countA -= 1 
        else:
            s+= 'B'
            countB -=1
        
        if countB == 0 and countA > 0:
            s+='A'
            countA -= 1
        elif countA == 0 and countB>0:
            s+='B'
            countB -= 1
        elif countA > countB:
            appendA = True 
        else:
            appendA = False
    
    return s 

