
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self,root:TreeNode):
        def dfs(node,cur,prev,level):
            if not node:
                return level
            elif cur=="start" and prev == "start":
                level=0
            elif cur!=prev:
                level+=1
            else:
                level=1
            
            return max(dfs(node.left,"left",cur,level),dfs(node.right,"right",cur,level))
        
        return dfs(root,"start","start",0)



