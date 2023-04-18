# python program to determine if two trees are identicl
# a binary tree node has data, pointer to left
# and a pointer to right child

class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=None
        self.right=None

# given two trees, return true if they are structurally
# identical
def identicalTrees(a,b):
    if a is None and b is None:
        return True
    # both non - empty -> compare them
    if a is not None and b is not None:
        return ((a.data==b.data) and identicalTrees(a.left,b.left) and identicalTrees(a.right,b.right))
    
    return False