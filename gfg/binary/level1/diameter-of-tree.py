"""
Python program to find diameter 
of a binary tree.

"""
class newNode:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = self.right = None
    
def height(root,ans):
    left_height = height(root.left, ans)
    right_height = height(root.right, ans)
    """Update the answer, because diameter
    of a tree is nothinng but maximum value of
    (left_height + right_height +1) for each node"""
    ans[0] = max(ans[0], 1+left_height+right_height)

    return 1+max(left_height,right_height)

# Computes the diameter of binary 
# tree with given root.

def diameter(root):
    if (root == None):
        return 0
    ans = [-999999999999]
    height_of_tree = height(root, ans)
    return ans[0]


