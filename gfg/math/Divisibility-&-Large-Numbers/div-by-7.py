# Program to check  whether a number is divisible
# by 7 or not

def isDivisibleBy7(num):
    # if number is negative, make it positive
    if num<0:
        return isDivisibleBy7(-num)
    # Base case 
    if (num==0 or num==7):
        return True
    
    if (num<10):
        return False
    return isDivisibleBy7(num//10 - 2*(num-num))
