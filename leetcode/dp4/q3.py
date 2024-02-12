
def binary_search(arr):
    n=len(arr)
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]==n-mid:
            return n-mid
        elif arr[mid]< n-mid:
            low=mid+1
        else:
            high=mid-1
    return n-low

arr=[1,1,1,2,100]

print(binary_search(arr))


