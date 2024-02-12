intervals=[[3,4],[2,3],[1,2]]
n=len(intervals)
start_points={}
for i,interval in enumerate(intervals):
    start_points[interval[0]]=i

sorted_list=sorted(intervals,key=lambda x:x[0])

def binary_search(element:list):
    left,right=0,n
    while left<right:
        mid=(left+right)//2
        if sorted_list[mid][0]<element[1]:
            left=mid+1
        else:
            right=mid
    return left

ans=[-1]*n
for i,interval in enumerate(intervals):
    index=binary_search(interval)
    print(index)
    if index<n:
        ans[i]=start_points[sorted_list[index][0]]

print(sorted_list,ans)
