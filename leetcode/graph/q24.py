
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    

class Solution:
    def delNodes(self,root:TreeNode,to_delete:list[int]):
        ans=list()

        del_set=set(to_delete)

        def dfs(node:TreeNode,is_root:bool):
            if not node:
                return None
            
            can_delete=node.val in del_set

            if is_root and not can_delete:
                ans.append(node)
            
            node.left = dfs(node.left,can_delete)
            node.right = dfs(node.right,can_delete)

            return None if can_delete else node
        
        dfs(root,True)

        return ans



