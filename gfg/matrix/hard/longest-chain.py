"""
Longest chain of arr[i],arr[arr[i]],.. without repetition

"""
def anesting(arr,start,max):
    c_max=0
    # if current element is not visited then increase c_max by one, set
    # arr[start] and change the start to current value.
    while (arr[start]!=-1):
        c_max+=1
        temp=arr[start]
        arr[start]=-1
        start=temp
        
