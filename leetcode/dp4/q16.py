
def min_swap(arr):
    n=len(arr)
    indexed_arr=[(arr[i],i) for i in range(n)]
    indexed_arr.sort(key=lambda x:x[0])

    visited = [False]*n
    swaps=0

    for i in range(n):
        if visited[i] or indexed_arr[i][1]==i:
            continue
        cycle_size=0
        j=i
        while not visited[j]:
            visited[j]=True
            j=indexed_arr[j][1]
            cycle_size+=1
        swaps+=(cycle_size-1)
    return swaps


