from collections import defaultdict

class Solution:
    def maxScore(self,edges:list[list[int]],values:list[int]):
        tree=defaultdict(list)
        n=len(len(edges)+1)
        vis=[0]*n

        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        @cache
        def dfs(i,takes):
            if len(tree[i])==1 and vis[tree[i][0]]:
                vis[i]=1
                return values[i] if takes==1 else 0
            
            pick=values[i]
            notPick=0
            for j in tree[i]:
                if not vis[j]:
                    vis[j]=1
                    pick+=dfs(j,takes)
                    if not takes:
                        notPick+=dfs(j,takes+1)
                    vis[j]=0
            
            return max(pick,notPick)
        
        vis[0]=1
        return dfs(0,0)

        pass


