from collections import defaultdict

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self,root:TreeNode):
        dc=defaultdict(int)

        def dfs(node,level):
            if node:
                dc[level]+=node.val
            
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        
        dfs(root)
        ans=1
        mx=dc[1]
        for lev,val in dc.items():
            if val>mx:
                mx=val
                ans=lev
        
        return ans


