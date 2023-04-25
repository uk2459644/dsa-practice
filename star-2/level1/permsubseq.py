"""
Explanation:

LEt's count permutations of length 1,2,3,...,n separately
and add them up.

For a permutation of length K, we need to:
- choose exactly one 1
- choose exactly one 2
- choose exactly one 3
...
- choose exactly one K

There are no further restrictions, since the order of the chosen elements
doesn't matter.

In particular, if there are freq[i] occurences of element i in the array,
then the number of ways to do the above is simply freq[1]Xfreq[2]Xfreq[3]X...Xfreq[k]
=
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=10000000007
    d={}
    for i in l:
        if i in d:
            d[i]+=1 
        else:
            d[i]=1 
    x=1 
    c=0
    p=1 
    while (x in d) and d[x]>0:
        cur=((p%m)*(d[x]%m))%m
        c+=cur
        p=cur
        c=c%m
        x+=1 
    print(c)
