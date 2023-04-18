
# A binary tree node 
class Node:
    # Constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None

# Binary search tree 
class BinarySearchTree:
    # Constructor to create a new BST 
    def __init__(self) -> None:
         self.root = None
    
    # function to insert an element in BST 
    def insertRec(self,root, data):
        if root is None:
            root = Node(data)
            return root
        # otherwise recur down the tree
        if data < root.data:
            root.left = self.insertRec(root.left,data)
        elif data > root.data:
            root.right = self.insertRec(root.right, data)
        
        return root
    
    # Function to insert an element in BST 
    def insert(self,data):
        self.root = self.insertRec(self.root, data)
    # Function to check if pair is present
    def isPairPresent(self,root,temp,target):
        if temp is None:
            return False
    
    # Function to search an element in BST
    def search(self, root, temp,k):
        # Base case 
        if root is None:
            return False
        c= root
        flag = False 
        while c is not None and flag == False:
            if c.data == k and temp!=c:
                flag = True
                print("Pair found: ", c.data, "+", temp.data)
                return True
            elif k<c.data:
                c=c.left
            else:
                c=c.right 
        return False

