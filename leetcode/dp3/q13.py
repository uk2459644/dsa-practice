
nums=[5,9,18,54,108,540,90,180,360,720]
nums.sort()
n=len(nums)
res=[[num] for num in nums]
# ans=[]
for i in range(n):
    for j in range(i):
        if (nums[i]%nums[j])==0 and len(res[i])<len(res[j])+1:
            res[i]=res[j]+[nums[i]]

print(max(res,key=len))