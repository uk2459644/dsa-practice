import bisect

arr=[1,2,3,4,5]
k=4
x=-1

position = bisect.bisect_right(arr,x)
ans=[]
n=len(arr)
j=position
i=position-1

while k>0:
    if i>=0 and j<n:
        if abs(arr[i]-x)<=abs(arr[j]-x):
            ans.append(arr[i])
            i-=1
            k-=1
        else:
            ans.append(arr[j])
            j+=1
            k-=1
    elif i<0:
        ans+=arr[:k]
        break

print(ans,len(ans))







