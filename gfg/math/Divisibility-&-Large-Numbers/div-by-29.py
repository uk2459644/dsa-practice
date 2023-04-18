# A quick solution to check if a number
# is divisible by 29 or not is to add 3
# times of alst digit to rest number and repeat
# this process untill number comes 2 digit. 

# Given number is divisible by 29, if the obtained two digit
# number is divisible by 29.

def isDiv(n):
    while (int(n/100)):
        last_digit = int(n%10)
        n=int(n/10)
        n+=last_digit*3 
    
    return (n%29==0)

