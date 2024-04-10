
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self,root:TreeNode):
        ans=0
        def dfs(node,parent,grand):
            nonlocal ans
            if not node:
                return
            
            if grand and grand.val%2==0:
                ans+=node.val
            
            if node.left:
                dfs(node.left,node,parent)
            if node.right:
                dfs(node.right,node,parent)
        
        dfs(root,None,None)

        return ans


