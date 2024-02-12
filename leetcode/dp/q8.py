nli=list(map(int,input().split()))
length=len(nli)
pos=0
count=0

def minJump(arr,pos,count):

    if arr[pos]+count>=(length-1):
        count+=1
        return 
    
    for j in range(arr[pos]):
        minJump(arr,pos+j,count+1)

ans=minJump(nli,pos,count)

print(ans)
    