class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def solve(self,root:TreeNode,k:int):
        self.ans=-1
        self.k=k

        def dfs(node):
            if node:
                dfs(node.left)
                self.k-=1
                if self.k==0:
                    self.ans=node.val
                dfs(node.right)
        
        dfs(root)

        return self.ans
        



