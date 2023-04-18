# python program to convert a binary
# tree to its mirror

# utility function to create a new tree node

class newNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None
    
def mirror(node):
    if (node == None):
        return
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)

        temp= node.left
        node.left = node.right
        node.right = temp

def inOrder(node):
    if (node == None):
        return
    
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)
    