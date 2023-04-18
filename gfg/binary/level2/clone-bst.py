# A hashmap based program to clone a binary tree with
# random pointers 

class Node:
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None 
        self.right = None
        self.random = None

# Helper function that allocates a new Node with the 
# given data and Node left, right and random pointers

def new_node(key):
    temp = Node(key)
    return temp

# Given a binary tree, print its Nodes in inorder 

def print_inorder(node):
    if node == None:
        return 
    # first recur on left subtree 
    print_inorder(node.left)
    # then print data of Node and its random 
    print("[", node.key, end=", ")
    if node.random == None:
        print("None],", end="")
    else:
        print(node.random.key,"], ",end="")
    # now recur on right subtree 
    print_inorder(node.right)

# This function creates clone by coping key 
# and left and right pointers. This function also
# stores mapping from given tree node to clone 

def copy_left_right_node(tree_node, mymap):
    if tree_node == None:
        return None 
    clone_node = new_node(tree_node.key)
    mymap[tree_node] = clone_node
    clone_node.left = copy_left_right_node(tree_node.left)
    clone_node.right = copy_left_right_node(tree_node.right)

    return clone_node

# This function copies random node by using the hashmap
# built by copy_left_right_node()

def copy_random(tree_node, mymap):
    if tree_node is None:
        return 
    if tree_node.random is not None:
        mymap[tree_node].random = mymap[tree_node.random]
    
    copy_random(tree_node.left,mymap)
    copy_random(tree_node.right,mymap)


