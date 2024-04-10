
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode):
        ans=[]

        def dfs(node):
            if node!=None:
                ans.append(node.val)
                if node.left != None:
                    dfs(node.left)
                
                if node.right != None:
                    dfs(node.right)
        
        dfs(root1)
        dfs(root2)
        ans.sort()

        return ans


