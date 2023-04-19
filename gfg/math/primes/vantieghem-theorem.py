"""
Vantiegham's Theorem is a necessary and sufficient
condition for a number to be prime. IT states that for a 
natural number n to be prime, the product of .
"""

def checkVantieghemsTheorem(limit):
    prod=1
    for n in range(2,limit):
        # check if above condition is satisfied
        if n==2:
            print(2,"is prime")
        
        if (((prod-n)%((1<<n)-1))==0):
            print(n,"is prime")
        
        prod*=((1<<n)-1)