def clc(arr):
    cnt=0
    nm=len(arr)
    for i in range(1,nm):
        if arr[i]!=arr[i-1]:
            cnt+=1 
        else:
            cnt+=2
    return cnt

for _ in range(int(input())):
    n,k=map(int,input().split())
    qli=[int(a) for a in input()]
    kli=list(map(int,input().split()))
    ans=clc(qli)
    for j in kli:
        j-=1 
        if qli[j]==0:
            qli[j]=1
        else:
            qli[j]=0
        
        if j>0:
            if qli[j]==qli[j-1]:
                ans+=1
            else:
                ans-=1
        if j<(n-1):
            if qli[j]==qli[j+1]:
                ans+=1
            else:
                ans-=1
        print(ans)