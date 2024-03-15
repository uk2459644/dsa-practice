
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(sel,root:TreeNode,distance:int):
        ans=0

        def dfs(node):
            nonlocal ans
            if node == None:
                return []
            
            if node.left ==  None and node.right == None:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)

            for i in left:
                for j in right:
                    if i+j<=distance:
                        ans+=1
            
            new_list=[]
            for i in left+right:
                if i+1<distance:
                    new_list.append(i+1)
            
            return new_list
        dfs(root)

        return ans


