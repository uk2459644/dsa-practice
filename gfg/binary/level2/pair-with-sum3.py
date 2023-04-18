# In a balanced binary search tree 
# isPairPresent two element which sums to 
# a given value time O(n) space O(logn)

MAX_SIZE = 100

# A BST node
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = self.right = None

# Stack type
class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.top = 0
        self.array = []

# A utility function to create a stack of given size
def createStack(size):
    stack = Stack()
    stack.size = size
    stack.top = -1 
    stack.array = [0 for i in range(stack.size)]
    return stack

# Basic operations of stack 
def isFull(stack):
    return 1 if (stack.top -1 == stack.size) else 0

def isEmpty(stack):
    return 1 if stack.top == -1 else 0

def push(stack,node):
    if (isFull(stack)==1):
        return 
    stack.array[stack.top+1] = node
    stack.top +=1 

def pop(stack):
    if (isEmpty(stack)==1):
        return None 
    x=stack.array[stack.top]
    stack.top -= 1
    return x

# Retursn true is a pair with target
# sum exists in BST, otherwise False 

def isPairPresent(root, target):
    # Create two stacks. s1 is used for 
    # normal inorder traversal and s2 is used for reverse
    # inorder traversal
    s1=createStack(MAX_SIZE)
    s2=createStack(MAX_SIZE)
    

