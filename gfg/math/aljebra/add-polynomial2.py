"""
The function first checks the lengths of the
two input lists and pads the sorter list with zeros so 
that both lists have same length. we then use the zip function
to create pairs of corresponding coefficients from the two
input lists, and the sum function to add the pairs together.
"""
def add_polynomials(p1,p2):
    len1,len2=len(p1),  len(p2)
    
    if len1 < len2:
        p1+=[0]*(len2-len1)
    else:
        p2+=[0]*(len1-len2)
    
    return [sum(x) for x in zip(p1,p2) ]

