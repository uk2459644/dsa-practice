# python program to find the maximum depth of tree
#  a binary tree

class Node:
    # def constructor to create a new node
    def __init__(self,data) -> None:
        self.data=data
        self.left = None
        self.right = None

# calculate the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the 
# farthest leaf node

def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth>rDepth):
            return lDepth+1
        else:
            return rDepth+1

# Driver program to test above function

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of tree is %d" % (maxDepth(root)))
