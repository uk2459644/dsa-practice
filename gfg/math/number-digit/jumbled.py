"""
Write a program to check if a given integer is 
jumbled or not. A number is said to be jumbled if for
every digit, its neighbours digit differs by max 1.

"""

def checkJumbled(num):

    # Single digit number
    if (num//10==0):
        return True 
    
    # Checking every digit
    # through a loop
    while (num!=0):
        # all digits were checked
        if (num//10==0):
            return True
        
        # digits at index i
        digit1 = num%10 
        digit2=(num//10)%10 

        if (abs(digit2-digit1)>1):
            return False 
        
        num=num//10
    
    return True

    
