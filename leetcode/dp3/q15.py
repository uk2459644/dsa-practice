nums=[4,3,2,6]
n=len(nums)
prev=0
for i in range(n):
    prev+=i*nums[i]

ans=prev
curr=0
for i in range(1,n):
    last_elem=nums[-1]
    rest_list=nums[:-1]
    curr=(prev-(n-1)*last_elem)+sum(rest_list)
    ans=max(ans,curr)
    prev=curr
    curr=0
    nums=[last_elem]+rest_list


print(prev,ans)


