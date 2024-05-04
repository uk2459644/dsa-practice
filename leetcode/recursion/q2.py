n=6
k=5
lst=[(i+1) for i in range(n)]
print(lst)
ind=0
while len(lst)>1:
    ind=(ind+k-1)%len(lst)
    del lst[ind]

# return lst[0]
print(lst)