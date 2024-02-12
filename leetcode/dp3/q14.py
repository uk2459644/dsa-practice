
nums=[2,3,6,7]
target=7

combination={}

def dfs(wanted):
    if wanted<0:
        return 0
    elif wanted==0:
        return 1
    
    if wanted in combination:
        return combination[wanted]
    
    count=0
    # ans=[]
    for num in nums:
        next_wanted=wanted-num
        count+=dfs(next_wanted)
        
    
    combination[wanted]=count
    return count

print(dfs(target))

    




