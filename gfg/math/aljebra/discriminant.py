"""
- If the discriminant is equal to zero then one
   solution is possible.

- If the discriminant is positive then two solutions are
   possible

- If the discriminant is negative then no real solutions are possible

"""

def discriminant(a,b,c):
    discriminant = (b**2)-(4*a*c)

    if discriminant > 0:
        print('Two solutions')
    elif discriminant == 0:
        print('One solution')
    elif discriminant <0:
        print('No real solutions.')
        