class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delLeafNodes(self,root:TreeNode,target:int):

        def dfs(root,val):
            if not root:
                return root
            
            if root.left is not None and root.right is not None and root.val == val:
                return None
            
            root.left = dfs(root.left,val)
            root.right = dfs(root.right,val)

            if root.left is not None and root.right is not None and root.val == val:
                return root
            
            return root
        
        return dfs(root,val)



