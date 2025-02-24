# Basics about Python Classes

# A class in Python is a blueprint for creating objects. When you define a class, 
# you specify what attributes (data) and methods (functions) the objects of 
# that class will have. This is especially useful in binary trees where each node is 
# an object with its own value and pointers to left and right children.

# The __init__ Method and self

# __init__ method: This is the constructor method that initializes a new object of the class. 
# When you create a new object, Python automatically calls this method.
# self: The first parameter in the __init__ method (and any method) always refers to the 
# current instance of the class. It allows you to set or access attributes of the object.

class Node:
    def __init__(self, value):
        self.value = value  # Instance attribute to store the node's value
        self.left = None    # Pointer to the left child (initially None)
        self.right = None   # Pointer to the right child (iniitially None)


# Creatinga dn Using an Instance

# Once you have defined your class, you create an instance (or object) of that class
# name like a function:

root = Node(10)

# Here, root is an object of type Node with a value of 10, and its left 
# and right children are initially None.


# Accessing Attributes and Methods
# You access attributes and methods of an instance using the dot (.) operator:

print(root.value)   # Points: 10
root.left = Node(5) # Creates a left child node with value 5

