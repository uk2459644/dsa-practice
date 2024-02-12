
nli=list(map(int,input().split()))
n=len(nli)

def solve(arr:list,l,r):
    if l>r:
        return True
    if l==r:
        return True
    ans=False
    for i in range(l+1,l+arr[l]+1):
        ans=ans or solve(arr,i,r)

    return ans
print(solve(nli,0,n-1))
    


