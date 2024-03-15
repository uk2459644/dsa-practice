
from collections import defaultdict,Counter

from typing import List

class UnionFind:
    def __init__(self,n):
        self.root=list(range(n))
    
    def find(self,x):
        if x!=self.root[x]:
            self.root[x]=self.find(self.root[x])
        
        return self.root[x]

    
    def union(self,x,y):
        self.root[self.find(x)]=self.find(y)

class Solution:
    def mhD(self,source:List[int],target:List[int],allowedSwaps:List[List[int]]):
        uf=UnionFind(len(source))
        # Perform uion based on allowed swaps
        for x,y in allowedSwaps:
            uf.union(x,y)
        
        m=defaultdict(set)

        for i in range(len(source)):
            m[uf.find(i)].add(i)
        
        ans=0

        for indices in m.values():
            A=[source[i] for i in indices]
            B=[target[i] for i in indices]

            ans += sum((Counter(A)-Counter(B)).values())
        
        return ans





