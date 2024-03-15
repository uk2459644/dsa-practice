class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def createBinaryTree(self,description:list[list[int]]):
        tracker={}
        not_root=set()

        for p,c,l in description:
            if p not in tracker:
                tracker[p]=TreeNode(p)
            if c not in tracker:
                tracker[c]=TreeNode(c)
            if l==1:
                tracker[p].left=tracker[c]
            else:
                tracker[p].right=tracker[c]
            
            not_root.add(c)
        for node in tracker.keys():
            if node not in not_root:
                return tracker[node]
                



