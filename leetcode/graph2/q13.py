
arr =[2,2,2]

n=len(arr)
inc,dec=0,0
ans=0

for i in range(1,n):
    if arr[i]>arr[i-1]:
        if dec>0:
            ans=max(ans,inc+dec+1)
            dec=0
            inc=0
        inc+=1
    elif arr[i]<arr[i-1]:
        if inc>0:
            dec+=1
    else:
        inc=0
        dec=0

print(ans)

