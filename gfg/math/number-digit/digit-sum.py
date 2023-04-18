"""
Program to find number of digit such that
integer - digitSum > s
"""

def digitSum(n):
    difSum=0
    while (n>0):
        difSum+=n%10
        n//=10
    return difSum

# Function to calculate count of integer s,

def countInteger(n,s):
    # if n < s no integer possible
    if (n<s):
        return 0
    
    for i in range(s,min(n,s+163)+1):
        if ((i-digitSum(i))>s):
            return (n-i+1)
    
    return 0
