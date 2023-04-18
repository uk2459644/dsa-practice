"""
Given a number and no. of digits to represent the number,
find if the given number can be represented in given
no. of digits in any base from 2 to 32

"""
"""
The idea is to check all bases one by one starting from
base 2 to base 32. How do we check for a given base?

Following are simple steps.

- If the number is smaller than the base and the digit
  is 1, then return true.

- Else if the digit is more than 1 and the number is more
  than base, then remove the last digit from num by doing num/base
  reduce the number of digits and recur.

  - Else return false

"""

def checkUtil(num,dig,base):
    # Base case 
    if (dig==1 and num<base):
        return True 
    
    if (dig>1 and num>=base):
        return checkUtil(num/base, --dig,base)
    
    return False
