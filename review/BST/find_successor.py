class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def _add(self, node, new_node):
        if node.element < new_node.element:
            if node.right == None:
                node.right = new_node
                return new_node
            else:
                return self._add(node.right, new_node)
        else:
            if node.left == None:
                node.left = new_node
                return new_node
            else:
                return self._add(node.left, new_node)
    
    def add(self, element):
        new_node = Node(element)
        if self.root == None:
            self.root = new_node
        else:
            return self._add(self.root, new_node)
            
    def leftMostChild(self, node):
        if node == None:
            return node
        while node.left:
            node = node.left
        return node
        
    def getSuccessor(self, node):
        if node == None:
            return None
        if node.right:
            return self.leftMostChild(node.right)
        return self.search(self.root, node.element, None)
    """
        Note: always keep in mind the in-order traversal to verify whether or not the parent or anccestor has been visited.
        if a given node does have a right subtree, then traverse from root to the given node and find
        closest left reference to the given node
    """
    def search(self, node, key, succ):
        if node == None:
            return None
        if node.element == key:
            return succ
        if node.element < key:
            return self.search(node.right, key, succ)
        if node.element > key:
            # if a left ref leads to the target node then update the succ 
            return self.search(node.left, key, node)
            

# b = BST()
# b.add(50)
# lola = b.add(40)
# b.add(20)
# b.add(46)
# b.add(5)
# b.add(25)
# b.add(41)
# b.add(6)
# b.add(42)
# b.add(67)
# successor = b.getSuccessor(lola)
                