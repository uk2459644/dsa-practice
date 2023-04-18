"""
GCD of three or more numbers equals the product of the prime
factors common to all the numbers, but it can also be 
calculated by repeatedly taking the GCDs of pairs of numbers.
"""
def find_gcd(x,y):
    while (y):
        x,y=y,x%y
    return x

l=[2,3,4,6,8,16]
num1=l[0]
num2=l[1]

gcd=find_gcd(num1,num2)
for i in range(num1,num2):
    gcd = find_gcd(gcd,l[i])

print(gcd)
