
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def flipTree(self,root1:TreeNode,root2:TreeNode):

        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            
            if not (node1 or node2) or node1.val != node2.val:
                return False
            
            check1=dfs(node1.left,node2.left) and dfs(node1.right,node2.right)
            check2=dfs(node1.right,node2.left) and dfs(node1.left,node2.right)

            return check1 or check2
        
        return dfs(root1,root2)
        



