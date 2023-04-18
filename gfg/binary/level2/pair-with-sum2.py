# Python3 code to find a pair with given sum
# in a balanced BST 

class Node:
    # Construct to create a new node
    def __init__(self, key) -> None:
        self.data = key 
        self.left = self.right = None

# A utility function to insert a new 
# Node with given key in BST 
def insert(root:Node, key:int):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)
    # Otherwise, recur down the tree 
    if root.data > key:
        root.left = insert(root.left, key)
    elif root.data < key:
        root.right = insert(root.right,key)
    
    # return the (unchanged) Node pointer
    return root

# Function that adds values of given BST into
# ArrayList and hence returns the ArrayList

def tree_to_list(root: Node, arr:list):
    if not root:
        return arr
    
    tree_to_list(root.left, arr)
    arr.append(root.data)
    tree_to_list(root.right, arr)

    return arr

# Function to check if there is a pair present
def isPairPresent(root:Node, target:int)->bool:
    # The list a1 is passed as an argument in 
    # treeToList mehtod is later
    # on filled by the values of BST
    arr1=[]
    # a2 list contains all the values of BST
    # returned by treeToList method
    arr2=tree_to_list(root,arr1)
    # starting index of a2
    start = 0
    # Ending index of a2
    end = len(arr2)-1 
    while start<end:
        # if target found 
        if arr2[start]+arr2[end]==target:
            print("Pair found",arr2[start],arr2[end])
            return True
        # Decrements end
        if arr2[start] + arr2[end]<target:
            end-=1 
        # Increments start
        if arr2[start]+arr2[end]<target:
            start+=1 
    
    print("No such values are found!")
    return False

