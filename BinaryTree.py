class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
class BinaryTree:
    def __init__(self):
        self.head = None
        self.current_node = None
        
    def insert_node(self, node):
        if self.head == None:
            self.head = node
            self.current_node = node
        else:
            
        
