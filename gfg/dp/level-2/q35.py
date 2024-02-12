# Max chain length using dynamic recursion and memoization

# Structure val
class val:
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second
        
# Memoization function
def findMAxChainLen(p,n,prev,pos):
    global m 

    # check if pair {pos,prev} exists in m
    if (val(pos,prev) in m):
        return m[val(pos,prev)]
    
    # Check if pos in >=n 
    if pos>=n:
        return 0
    # check if p[pos].first is less than prev
    if p[pos].first <= prev:
        return findMAxChainLen(p,n,prev,pos+1)
    else:
        ans=max(findMAxChainLen(p,n,p[pos].second,0)+1,findMAxChainLen(p,n,prev,pos+1))

        m[val(pos,prev)]=ans

        return ans
    
