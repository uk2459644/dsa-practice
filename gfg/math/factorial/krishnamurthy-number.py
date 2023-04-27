"""
A krishnamurthy number is a number whose sum of the factorial of digits 
is equal to the number itself. 
"""
def factorial(n):
    fact=1
    while (n!=0):
        fact=fact*n
        n=n-1
    
    return fact

def isKrishnamurthy(n):
    sum=0
    temp=n

    while (temp!=0):
        rem=temp%10
        sum+=factorial(rem)

        temp//=10
    
    return sum==n

