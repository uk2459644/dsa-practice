nums=[4,6,7,7]
lst=list()
n=len(nums)
base=nums[0]
lst.append(base)
for i in range(1,n):
    if base <= nums[i]:
        lst.append(nums[i])
m=len(lst)

def solve(i,ans:set):
    if i >= m:
        return ans
    
        