"""
Given a range L,R find total such numbers in the 
given range such that they have no repeated digits.

"""

""""
Brute Force 

We will traverse through each element in the given range
and count the number of digits which do not have repeated
digits.
"""

def repeated_digit(n):
    a=[]
    # traverse through each digit
    while n!=0:
        d=n%10

        if d in a:
            return 0
        a.append(d)
        n=n//10 
    
    return 1 

def calculated(L,R):
    answer=0
    for i in range(L,R+1):
        answer+=repeated_digit(i)
    
    return answer
