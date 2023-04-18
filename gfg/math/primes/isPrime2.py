"""
We will deal with a few numbers such as 1,2,3 and the numbers which are divisible by 2 nd 3
in separate cases and for remaining numbers. Iterate from 5 to sqrt(n) and
check for each iteration whether that value or that value +2 divides n or not
and increment the value by 6 [because any prime can be expressed as 6n+1 or
6n-1]. If we find any number that divides, we return false.


"""
import math

def isPrime(n:int)->bool:
    if n<=1:
        return False
    
    if n==2 or n==3:
        return True 
    
    if n%2 == 0 or n%3==0:
        return False 
    
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False 
    
    return True

