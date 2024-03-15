from collections import defaultdict

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def amountOfTime(self,root:list[TreeNode],start:int):
        graph=defaultdict(list)

        def dfs(node,parent):
            if node:
                if parent:
                    graph[node.val].append(parent)
                    graph[parent].append(node.val)
                
                if node.left:
                    dfs(node.left,node.val)
                if node.right:
                    dfs(node.right,node.val)
        
        dfs(root,None)
        visited=set()

        def dfs2(node,level):
            visited.add(node)
            ans=level
            for v in graph[node]:
                if v not in visited:
                    ans=max(ans,dfs2(v,level+1))
        
        return dfs2(start,0)




