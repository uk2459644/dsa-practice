

n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

def calculateTime(n):
    if manager[n]!=-1:
        informTime[n]+=calculateTime(manager[n])
        manager[n]=-1
    return informTime[n]

for i in range(len(manager)):
    calculateTime(i)

ans=max(informTime)



