class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def _add(self, node, new_node):
        if node.element < new_node.element:
            if node.right == None:
                node.right = new_node
                new_node.parent = node
                return new_node
            else:
                return self._add(node.right, new_node)
        else:
            if node.left == None:
                node.left = new_node
                new_node.parent = node
                return new_node
            else:
                return self._add(node.left, new_node)
    
    def add(self, element):
        new_node = Node(element)
        if self.root == None:
            self.root = new_node
        else:
            return self._add(self.root, new_node)
    
    
    # The tree is NOT a binary search tree. Therefore, we need to check if node in the tree
    # if one of the node does not exist in the tree that mean there is no LCA
    def commonAncesstor(self, root, p, q):
        if self.covers(root, p) == False or self.covers(root, q) == False:
            return False
        # Calling covers() function to see if p a child of q
        # if true, then p is LCA
        if self.covers(p, q):
            return p
        # Calling covers() function to see if q a child of p
        # if true, then q is LCA
        if self.covers(q, p):
            return q
        
        return self.getSibilings(p, q)
        
    #This function validate if both given nodes exist in the tree.
    # This tree is not Binary search tree so we have to look for both of them in the entire tree
    def covers(self, root, p):
        if root == None:
            return False
        if root == p:
            return True
        return self.covers(root.left, p) or self.covers(root.right, p)
    
    
    def getSibilings(self, p, q):
        node = p
        
        while node.parent != None:
            if node.parent.right == node:
                if self.covers(node.parent.left, q):
                    return node.parent
            if node.parent.left == node:
                if self.covers(node.parent.right, q):
                    return node.parent
            node = node.parent
        return False



    # This is another to solve it too.
    # Uncomment getSibilings() and commonAncesstor() functions and use the LCA() function
    # This approach is similiar to find if the binary search tree is balance 
    def LCA(self, p, q):
        if node == None:
            return 
        if self.covers(p, q):
            return node 
        if p.parent == None or p == q:
            return node
        return self.LCA(p.parent, q)
            


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
# b.commonAncesstor(b.root,p, q)

