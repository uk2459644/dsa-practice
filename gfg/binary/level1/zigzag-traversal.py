# program to print zigzag traversal 
# of binary tree 

# binary tree node
class Node:
    # constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = self.right = None

# function to print zigzag traversal of binary tree
def zigzagtraversal(root):
    if root is None:
        return
    # create two stack to store current
    # and next level 
    currentLevel = []
    nextLevel = []
    ltr= True
    currentLevel.append(root)

    while len(currentLevel)>0:
        temp = currentLevel.pop(-1)
        print(temp.data, " ",end="")
        if ltr:
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)
        
        if len(currentLevel) == 0:
            ltr = not ltr
            currentLevel, nextLevel =  nextLevel, currentLevel

