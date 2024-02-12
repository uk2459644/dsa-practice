
# Count Possible Decoding of a gien digit sequence

"""
This problem is recursive and can be broken innto sub-problems.
We start from the end of the given digit sequence. We initialize the total
count of decodings as 0. 

1-> If the last digit is non-zeror, recur for the remaining(n-1) 
    digits and add the result to the total count.

2-> If the last two digits form a valid character (or smaller than 27), recur
    for remaining (n-2) digits and add the result to the total count.

"""

# Recursive implementation of numDecodings

def numDecodings(s:str)->int:
    if len(s)==0 or (len(s)==1 and s[0]=='0'):
        return 0
    
    return numDecodingsHelper(s,len(s))

def numDecodingsHelper(s:str,n:int)->int:
    if n==0 or n==1:
        return 1
    
    count=0
    if s[n-1]>"0":
        count=numDecodingsHelper(s,n-1)
        if (s[n-2]=="1" or s[n-2]=="2" and s[n-1]<"7"):
            count+=numDecodingsHelper(s,n-2)
    
    return count


