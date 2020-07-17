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
                return new_node
            return self._add(node.right, new_node)
        else:
            if node.left == None:
                node.left = new_node
                return new_node
            return self._add(node.left, new_node)
    
    def add(self, element):
        new_node = Node(element)
        if self.root == None:
            self.root = new_node
            return self.root
        return self._add(self.root, new_node)

    def _search(self, node, element):
        if node.element == element:
            return True
        if node.element > element:
            return self._search( node.left, element)
        if node.element < element:
            return self._search(node.right, element)
        return False
    
    def search(self, element):
        if self.root:
            return self._search(self.root, element)
        return "Empy tree"
        
    
    def lowestCommonAncestor(self, root, p, q):
        if self.covers(root, p) == False or self.covers(root, q) == False:
            return False
        return self.ancestorHelp(root, p, q)
    
    def ancestorHelp(self, node, p, q):
        if node == None or node == p or node == q:
            return node
        pIsLeft = self.covers(node.left, p)
        qIsLeft = self.covers(node.left, q)
        
        if pIsLeft != qIsLeft:
            return node
        
        childSide = None
        if pIsLeft:
            childSide = node.left
        else:
            childSide = node.right
        return self.ancestorHelp(childSide, p, q)
    
    
    def covers(self, node, p):
        if node == None:
            return False
        if node == p:
            return True 
        return self.covers(node.left, p) or self.covers(node.right, p)



    """
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
            return self.root
        else:
            return self._add(self.root, new_node)
    
    def ancestorHelp(self, node, p, q):
        if node == None:
            return None
        if node == p and node == q:
            return node
        
        x = self.ancestorHelp(node.left, p, q)
        if x != None and x != p and x != q:
            return x
        
        y = self.ancestorHelp(node.right, p, q)
        if y != None and y != p and y != q:
            return y
        
        if x != None and y != None:
            return node
        elif node == p or node == q:
            return node
        else:
            if x == None:
                return y
            return x
            
            
# b = BST()
# b.add(50)
# b.add(40)
# b.add(20)
# b.add(45)
# b.add(5)
# q = b.add(25)
# b.add(41)
# p = b.add(6)
# b.add(42)
# b.add(55)
# b.ancestorHelp(b.root,p, q)
        
    """
        
        
        
        
b = BinarySearchTree()


