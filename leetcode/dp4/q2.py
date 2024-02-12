
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]>pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_select(arr,low,high,k):
    if low<=high:
        pivot_index=partition(arr,low,high)
        if pivot_index==k:
            return arr[pivot_index]
        elif pivot_index <k:
            return quick_select(arr,pivot_index+1,high,k)
        else:
            return quick_select(arr,low,pivot_index-1,k)

arr=[3,1,4,4,2,2,5,3]
k=4
result=quick_select(arr,0,len(arr)-1,k-1)

print(result)


