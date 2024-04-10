
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

        if root_x==root_y:
            return
        
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1

s = "pwqlmqm"
pairs = [[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]]
pairs.sort()
n=len(s)

uf=UnionFind(n)
for x,y in pairs:
    uf.union(x,y)

ans=[""]*n

for i in range(max(uf.parent)+1):
    indices=[]
    chars=[]
    for j in range(len(uf.parent)):
        if uf.parent[j]==i:
            indices.append(j)
            chars.append(s[j])
    chars.sort()
    ck=0
    for k in indices:
        ans[k]=chars[ck]
        ck+=1

res="".join(ans)
print(uf.parent,res,pairs)




