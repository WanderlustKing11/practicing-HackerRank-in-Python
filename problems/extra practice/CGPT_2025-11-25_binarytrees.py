# Binary Trees

# A binary tree consists of nodes, where each node can have a left child, 
# a right child, both, or no children. A typical Python class for a node looks like this:

class Node:
    def __init__(self, key):
        self.val = key      # The value stored in the node.
        self.left = None    # Pointer to the left child.
        self.right = None   # Pointer to the right child.


# Here, key is the value you want to store in the node. The left and right attributes 
# will point to other nodes or remain None if there are no children.


# 2. Inserting Nodes

# When working with binary trees, one common operation is insertion. For example, 
# in a binary search tree (BST), every node follows this rule:

# - The left child's value is less than the parent’s value.
# - The right child's value is greater than the parent’s value.

# Here's a simple recursive function to insert a new value into a BST:

def insert(root, key):
    # If the tree/subtree is empty, return a new node.
    if root is None:
        return Node(key)
    
    # Recursively insert the key into the left or right subtree.
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

# You would typically start with a root that might be None and then add values one by one.


# 3. Tree Traversals

# a. In-Order Traversal - For a BST, this returns the values in sorted order.
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# b. Pre-Order Traversal - This traversal visits the current node before its children.
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# c. Post-Order Traversal - This visits the children before the current node.
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")



###############################################################################

### Putting it all together

if __name__ == "__main__":
    # start with an empty tree
    root = None

    # List of values to insert
    values = [50, 30, 20, 40, 70, 60, 80]

    # Insert each value into the BST
    for val in values:
        root = insert(root, val)

    print("In-order Traversal:")
    inorder(root)   # Should print: 20 30 40 50 60 70 80 

    print("\nPre-order Traversal:")
    preorder(root)  # Order depends on tree structure

    print("\nPost-order Traversal:")
    postorder(root) # Order depends on tree structure