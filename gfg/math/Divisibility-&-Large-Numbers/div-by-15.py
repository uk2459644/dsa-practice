# Brute force approach

# Convert the input number to a string and remove
# any whitespace or special characters from it.

# initialize a variable sum to 0.

# iterate over each character in the string and convert it
# to an integer

# Add the integet to the sum\

# after iterating over all the characters, check if the sum is divisble
# by both 3 nd 5. If it is, return "YES",
# otherwise return "No".

# to find sum
def accumulate(s):
    acc=0
    for i in range(len(s)):
        acc+=ord(s[i])
    
    return acc

def isDivisible(s):
    n=len(s)
    if (s[n-1]!='5' and s[n-1]!='0'):
        return False
    
    sum=accumulate(s)

    return (sum%3==0)
