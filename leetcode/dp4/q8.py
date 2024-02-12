
pairs=[[1,2],[7,8],[4,5]]

n=len(pairs)
pairs.sort(key=lambda x:x[1])

base=pairs[0][1]
count=0

for i in range(1,n):
    if pairs[i][0]>base:
        count+=1
        base=pairs[i][1]


