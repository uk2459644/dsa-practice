upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]

n=len(colsum)

if upper>n or lower>n:
    return []

if (upper+lower)!=sum(colsum):
    return []

ans=[[0]*n for _   in range(2)]

for i in range(n):
    if colsum[i]==0:
        continue
    elif colsum[i]==2:
        ans[0][i]=1
        ans[1][i]=1
        lower-=1
        upper-=1
    elif colsum[i]==1:
        if upper>lower:
            ans[0][i]=1
            upper-=1
        else:
            ans[1][i]=1
            lower-=1
    
    if lower<0 or upper < 0:
        return []
return ans


