"""
One way to solve it is by finding GCD(x,y), and using it we find 
LCM(x,y). Similarly, we find LCM(x,z) and then we finally find the GCD of the obtained
results.

An efficient approach can be done by the fact that the
following version of distributivity holds true:

GCD(LCM(x,y),LCM(x,z))=LCM(x,GCD(y,z))

"""
def __gcd(a,b):
    # Everything divides 0
    if (b==0):
        return a 
    
    return __gcd(b,a%b)

def findValue(x,y,z):
    g=__gcd(y,z)
    return (x*g)/__gcd(x,g)

