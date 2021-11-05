class Node:
    def __init__(self, value, tree_level):
        self.value = value
        self.right = None
        self.left = None
        self.tree_level = tree_level



class BinaryTree:
    def __init__(self):
        self.root = None


    def add_node(self, value):
        if not self.root:
            self.root = Node(value, 1)

        else:
            done = False
            current_node = self.root
            tree_level = 2

            while not done:
                if value > current_node.value:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(value, tree_level)
                        done = True

                elif value < current_node.value:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(value, tree_level)
                        done = True

                tree_level += 1
                


def traverse_tree(node):
    if node:
        print(node.value, node.tree_level)
        
        traverse_tree(node.right)
        traverse_tree(node.left)
    


def find_element(root, element):
    if not root:
        return False

    else:
        if element == root.value:
            return True
        else:
            if element > root.value:
                return find_element(root.left, element)
            elif element < root.value:
                return find_element(root.right, element)

                
if __name__ == '__main__':
    tree = binary_tree()

    for number in [1, 4, 5, 3, 8, 10, 2, 7, 20, 17]: tree.add_node(number)

    print(find_element(tree.root, 9))

    
                
            
