"""
Given a set of n elements, find number of ways of partitioning it.

"""
"""
LEt S(n,k) be total number of a partitions of n elements into k sets. The value
of n'th Bell Number is sum of S(n,k) for k=1 to n.

Value of S(n,k) can be defined recursively as, S(n+1,k)=k*S(n,k)+S(n,k-1)

How does above recursive formula work?

When we add a (n+1)th element to k partitions, there are two possibilities.

1). It is added as a single element set to existing partitions, S(n,k-1)
2). It is added to all sets of every partition, i.e. k*S(n,k)
"""
n=5 
s=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if j>i:
            continue
        elif (i==j):
            s[i][j]=1
        else:
            s[i][j]=j*s[i-1][j]+s[i-1][j-1]

ans=0

for i in range(0,n+1):
    ans+=s[n][i]

print(ans)
