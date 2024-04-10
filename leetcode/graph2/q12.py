
arr =[2,1,4,7,3,2,5]

n=len(arr)

left=0
right=0
ans=0
for i in range(1,n-1):
    if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
        left=i
        right=i

        while left>0 and arr[left-1]<arr[left]:
            left-=1
        
        while right+1 < n and arr[right]>arr[right+1]:
            right+=1
    
    ans=max(ans,(right-left+1))

    


print(ans)
