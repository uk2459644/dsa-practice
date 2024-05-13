nums = [71,18,52,29,55,73,24,42,66,8,80,2]
k = 3

stack=[]
n=len(nums)
for i,num in enumerate(nums):
    while stack and stack[-1]>num:
        ln=len(stack)-1+n-i
        if ln<k:
            break
        stack.pop()
    stack.append(num)

print(stack[:k])

