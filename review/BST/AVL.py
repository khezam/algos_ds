class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def _add(self, node, new_node):
        if node.element < new_node.element:
            if node.right == None:
                node.right = new_node
                return node
            return self._add(node.right, new_node)
        else:
            if node.left == None:
                node.left = new_node
                return node
            return self._add(node.left, new_node)
    
    def add(self, element):
        new_node = Node(element)
        if self.root == None:
            self.root = new_node
            return self.root
        return self._add(self.root, new_node)
        
    def _search(self, node, element):
        if node.element == element:
            return node
        if node.element > element:
            return self._search( node.left, element)
        if node.element < element:
            return self._search(node.right, element)
        return False
    
    def search(self, element):
        if self.root:
            return self._search(self.root, element)
        return "Empy tree"
         
    def unbalanceSolution(self, nodeLeft, nodeRight):
        curr = nodeRight
        while curr.left:
            curr = curr.left
        curr.left = nodeLeft
        return nodeRight
        
    def balanceSolution(self, node):
        if node.left and node.left.left == None:
                successor = node.left.element
                node.left = None
                return successor
        if node.left == None:
            successor = node.element
            node = None
            return successor
        return self.balanceSolution(node.left)
        
    def _remove(self, node, element):
        if node.element == element:
            if node.left == None and node.right == None:
                return None
            if node.right == None or node.left == None:
                if node.right:
                    return node.right
                if node.left:
                    return node.left
            if node.right != None and node.left != None:
                # Causes unbalance tree
                # return self.unbalanceSolution(node.left, node.right)
                if node.right.left == None:   
                    node.element = self.balanceSolution(node.right)
                    node.right = None
                    return node
                node.element = self.balanceSolution(node.right)
                return node
        if node.element < element:
            node.right = self._remove(node.right, element)
            return node
        if node.element > element:
            node.left = self._remove(node.left, element)
            return node
        return "Not found"
        
    def remove(self, element):
        if self.root:
            return self._remove(self.root, element)
        return "Empty tree"
        
        
    # def is_balance(self, 

        
# b = BinarySearchTree()
# b.add(60)
# b.add(12)
# b.add(41)
# b.add(4)
# b.add(90)
# b.add(71)
# b.add(100)
# b.add(84)
# b.add(1)
# b.add(29)
# b.add(23)
# b.add(37)




        