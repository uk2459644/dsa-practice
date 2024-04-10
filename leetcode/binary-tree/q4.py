
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    
    def flipNode(self,root:TreeNode,voyage:list[int]):
        self.ans=[]
        self.p=0

        def dfs(root):
            if not root:
                return True
            
            if root.val != voyage[self.p]:
                return False
            
            self.p+=1
            if root.left and (root.left.val != voyage[self.p]):
                if root.right:
                    self.ans.append(root.val)
                root.left,root.right=root.right,root.left
            
            return dfs(root.left) and dfs(root.right)
        
        if dfs(root):
            return self.ans
        
        return [-1]



