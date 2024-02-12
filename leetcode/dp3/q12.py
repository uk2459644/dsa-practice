envelopes=[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
sorted_list=sorted(envelopes)
n=len(envelopes)
count=1
maxcount=1
prev=sorted_list[0]
for i in range(1,n):
    if (sorted_list[i][0]>prev[0]) and (sorted_list[i][1]>prev[1]):
        count+=1
        maxcount=max(count,maxcount)
        prev=sorted_list[i]
    
print(maxcount,sorted_list)

