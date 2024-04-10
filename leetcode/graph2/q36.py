

nums = [1,7,6,18,2,1]
limit = 3

n=len(nums)

# Create a list containing tuples of original array
b=[]
for i in range(n):
    b.append((nums[i],i))

b=sorted(b,key=lambda x:x[0])

groups=[[b[0]]]
for i in range(1,n):
    if b[i][0]-b[i-1][0]<=limit:
        groups[-1].append(b[i])
    else:
        groups.append([b[i]])

for group in groups:
    ind=[]
    for x,y in group:
        ind.append(y)
    ind.sort()
    for i in range(len(ind)):
        nums[ind[i]] = group[i][0]




print(nums)




