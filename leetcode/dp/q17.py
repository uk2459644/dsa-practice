import sys

nli=list(map(int,input().split()))
n=len(nli)
maxi=nli[0]

for i in range(1,n):
    maxi=max(maxi,maxi+nli[i])