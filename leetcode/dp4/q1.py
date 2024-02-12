
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        lesser=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:] if x> pivot]

        return quick_sort(lesser)+[pivot]+quick_sort(greater)

arr=[3,1,4,4,2,2,5,3]
sorted_arr=quick_sort(arr)
print(sorted_arr)
