from collections import defaultdict


nums = [2,4,3,3,5,4,9,6]
k = 4

stack,dict1=[],{j:i for i,j in enumerate(nums)}

dig_count=defaultdict(int)

for i,j in enumerate(nums):
    dig_count[j]+=1

    
    
    while stack and stack[-1]>j and dict1[stack[-1]]>i:
        stack.pop()
    if len(stack)<k:
        stack.append(j)
    else:
        stack.append(j)
        stack.pop(0)


print("hello from stack",stack)






