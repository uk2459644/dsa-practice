"""
Maximum chain length 

Method 2:

- Sort given pairs in increasing order of second values
- Take ans=0 initially and prev=INT_MIN
- Now iterate on the given array and if arr[i].first>prev, then increase 
  answer and set prev=arr[i].second 
- Finally return answer

"""
from typing import List, Tuple

def max_chain_len(p:List[Tuple[int,int]])->int:
    # Your code here
    p.sort(key=lambda x:x[1])
    pre=-1e9
    ans=0
    for x in p:
        if x[0]>pre:
            ans+=1
            pre=x[1]
    
    return ans


