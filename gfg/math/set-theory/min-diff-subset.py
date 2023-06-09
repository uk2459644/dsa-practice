"""
Given a number n, divide first n natural numbers (1,2,...n) into two subsets
such that difference between sums of two subsets is minimum.

Approach: 

The approach is based on the fact that any four consecutive numbers can be 
divided into two groups by putting middle two elements in one group and corner
elements in other group.So, if n is a multiple of 4 then their difference will be 0,
hence the summation of one set will be half of the summation of N elements which
can be calculated by using sum=n*(n+1)/2.

There are three other cases to consider in which we cannot divide into groups of 4,
which will leave remainder of 1,2 and 3:

a) If it leaves a remainder of 1, then all other n-1 elements are clubbed into
group of 4 hence their sum will be int(sum/2) and other half sum will be int(sum/2+1)
and their difference will be always be 1.

b) Above mentioned steps will be followed in case of n%4==2 also. Here we form groups of size 4
for elements from 3 onward. Remaining elements would be 1 and 2. 1 goes in one
group and 2 goes in other group.

c) When n%4 == 3, then club n-3 elements into groups of 4. The left out elements
will be 1,2 and 3, in which 1 and 2 will go to one set and 3 to other set, which 
eventually makes the difference to be 0 and summation of each set to be sum/2.

"""

def subsetDifference(n):
    s=int(n*(n+1)/2)

    if n%4==0:
        print("First subset sum=",int(s/2))
        print("Second subset sum", int(s/2))
        print("Difference",0)
    else:
        if n%4==1 or n%4==2:
            print("First subset sum=",int(s/2))
            print("Second subset sum=",int(s/2)+1)
            print("Difference=",1)
        else:
            print(0)


