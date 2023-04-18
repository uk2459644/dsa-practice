"""
Optimized approach 

we can optimize this program by adding a break 
statement in the check function to stop checking for
base once the number is found to be representable in
a given number of digits in a particular base.

Define the checkUtil function:

"""

def check_util(num,dig,base):
    # base case 
    if dig == 1 and num < base:
        return True 
    if dig>1 and num>=base:
        return check_util(num//base, dig-1,base)
    
    return False

def check(num,dig):
    for base in range(2,33):
        if check_util(num,dig,base):
            return True
        if base>=num:
            break
    
    return False
