from collections import defaultdict


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left =left
        self.right = right

class Solution:
    def deepestLeavesSum(self,root:TreeNode):
        nodeList=defaultdict(list)
        def dfs(node:TreeNode,level):
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
            
            nonlocal nodeList

            if node.left==None and node.right == None:
                nodeList[level].append(node.val)
        
        dfs(root,0)
        max_key = max(nodeList.keys())
        return sum(nodeList[max_key])
        
            


