nums=[1,2]
def solve(ind,cur):
    if ind>=len(nums):
        if len(cur)>1:
            return [cur]
        return []
    res=[]
    if not cur or cur[-1]<=nums[ind]:
        res += solve(ind+1,cur+[nums[ind]])
    if not cur or cur[-1]!=nums[ind]:
        res += solve(ind+1,cur)

    return res


