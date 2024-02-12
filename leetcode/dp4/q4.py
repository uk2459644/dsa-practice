
arr=[[1,2],[2,3],[3,4],[1,3]]
sorted_list=sorted(arr,key=lambda x:x[1])
# sorted_list=sorted(sorted_list,key=lambda x:x[1])
n=len(arr)
count=0

for i in range(n-1):
    if sorted_list[i+1][0]==sorted_list[i][0]:
        count+=1

print(sorted_list)

