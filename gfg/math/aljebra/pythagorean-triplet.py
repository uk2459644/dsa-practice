"""
Efficient solution can print all triplets in O(k) time
where k is number of triplets printed. The idea is to use
square sum relation of Pythagorean triplet, addition of squares of a and b
is equal to square of c, we cn write these number in terms of m and n.

a=m^2 - n^2 
b=2*m*n
c=m^2 + n^2 


"""

def pythagoreanTriplet(limits):
    c,m=0,2

    while c<limits:
        for n in range(1,m):
            a=m*m - n*n 
            b=2*m*n 
            c=m*m + n*n 

            if c>limits:
                break 
            print(a,b,c)
        m+=1 
    