
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxAncestorDiff(self,root:TreeNode):
        if not root:
            return 0
        
        ans=-1

        def dfs(node,mx,mn):
            if node:
                mx=max(node.val,mx)
                mn=min(node.val,mn)
                nonlocal ans
                ans=max(ans,abs(mx-mn))
                dfs(node.left,mx,mn)
                dfs(node.right,mx,mn)
        
        dfs(root,root.val,root.val)

        return ans


