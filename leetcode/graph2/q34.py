from collections import defaultdict

class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x == root_y:
            return False
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1
        
        return True

s = "pwqlmqm"
pairs = [[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]]

n=len(s)
uf=UnionFind(n)

for x,y in pairs:
    uf.union(x,y)

groups = defaultdict(list)

for i in range(n):
    groups[uf.find(i)].append(i)

ans=[ch for ch in s]

for i,group in groups.items():
    chars=[s[i] for i in group]
    chars.sort()
    for i,idx in enumerate(group):
        ans[idx]=chars[i]

res="".join(ans)

print(res)



