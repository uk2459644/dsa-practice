"""
The Fibonacci numbers are the numbers in the following
integer sequence.
0,1,1,2,3,5,8,13,21,34,.....

In mathmatical terms, the sequence Fn of Fibonacci numbers is
defined by the recurrence relation.

Fn=Fn-1 + Fn-2
where, F0=0 and F1=1

"""
# MEthod 1 : Recursion

def fibonacci(n):
    if n<=1:
        return n
    
    return fibonacci(n-1)+fibonacci(n-2)

# Method 2: Use Dynamic Programming
def fibonacci(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    
    return f[n]

# MEthod 3: Space Optimized method
# We can optimize the space used in method 2 by storing the previous
# two numbers only becuse that is all we need to get the next number in series

def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("Incorrect Input")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
    

