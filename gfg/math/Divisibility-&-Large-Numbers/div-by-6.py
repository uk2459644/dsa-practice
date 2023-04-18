# Python program to find if a number
# is divisible by 6 or not

# function to find that number is divisible 

def check(st):
    n=len(st)
    # Return false if number 
    # is not divisible by 2
    if (((int)(st[n-1])%2)!=0):
        return False
    
    # compute sum of digits
    digitSum = 0
    for i in range(0,n):
        digitSum = digitSum+(int)(st[i])
    
    # Check if sum of digits is divisible by 3
    return (digitSum%3==0)
