
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self,root:TreeNode,n:int,x:int):

        def size(r):
            if not r:
                return 0
            else:
                return 1+size(r.left)+size(r.right)
        
        def findx(r):
            if not r:
                return None
            elif r.val==x:
                return r
            else:
                return findx(r.left) or findx(r.right)
        
        x=findx(root)
        sizel=size(x.left)
        sizer=size(x.right)
        



