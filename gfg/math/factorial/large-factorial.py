import sys 

def factorial(n):
    res=[None]*500

    res[0]=1
    res_size=1

    x=2
    pass

def multiply(x,res,res_size):
    carry=0

    i=0
    while i<res_size:
        prod=res[i]*x + carry
        res[i]=prod%10 

        carry=prod//10
        i+=1
        