
rowSum=[]
colSum=[]

r=len(rowSum)
c=len(colSum)

ans=[[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        el=min(rowSum[i],colSum[j])
        ans[i][j]=el
        rowSum[i]-=el
        colSum[j]-=el

return ans

