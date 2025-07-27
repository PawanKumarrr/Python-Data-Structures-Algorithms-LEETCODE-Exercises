# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        

# class BinarySearchTree:
    ## WRITE BST CONSTRUCTOR HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################

class BinarySearchTree:
    def __init__(self):
        self.root = None


my_tree = BinarySearchTree()

print("Root:", my_tree.root)


 
"""
    EXPECTED OUTPUT:
    ----------------
    Root: None

"""