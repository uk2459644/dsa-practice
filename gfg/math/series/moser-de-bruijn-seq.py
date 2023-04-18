"""
Moser-de bruijn sequence is the sequence obtained by adding up the 
distinct powers of the number 4
"""

def gen(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    elif n%2==0:
        return 4*gen(n//2)
    elif n%2==1:
        return 4*gen(n//2)+1 
    