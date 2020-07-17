class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None

        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def _add(self, node, new_node):
        if node.element < new_node.element:
            if node.right == None:
                node.right = new_node
                new_node.parent = node
            else:
                return self._add(node.right, new_node)
        else:
            if node.left == None:
                node.left = new_node
                new_node.parent = node
            else:
                return self._add(node.left, new_node)
            
        return self.is_balance(new_node)
    
    def add(self, element):
        new_node = Node(element)
        if self.root == None:
            self.root = new_node
            return self.root
        return self._add(self.root, new_node)
        
        
    def is_balance(self, node):
        left = self.height(node.left)
        right = self.height(node.right)
        if (left - right) > 1:
            if node.left.left:
                return self.rightRotate(node)
            if node.left.right:
                return self.leftRightRotate(node)
        if (left - right) < -1:
            if node.right.right:
                return self.leftRotate(node)
            if node.right.left:
                return self.rightLeftRotate(node)
        
        if node.parent == None:
            return 
        return self.is_balance(node.parent)
    
    def rightRotate(self, node):
        tmp = node.left
        node.left = tmp.right
        if node.left:
            node.left.parent = node
        tmp.right = node
        tmp.parent = node.parent
        # node.parent = tmp
        if tmp.parent == None:
            self.root = tmp
        if node.parent:
            node.parent.right = tmp
        node.parent = tmp
        return tmp
    
    def leftRotate(self, node):
        tmp = node.right
        node.right = tmp.left
        if node.right:
            node.right.parent = node
        tmp.left = node
        tmp.parent = node.parent
        node.parent = tmp
        if tmp.parent == None:
            self.root = tmp
        # if node.parent:
        #     node.parent.left = tmp
        # node.parent = tmp
        return tmp
        
    def rightLeftRotate(self, node):
        curr = node.right
        tmp = curr.left
        curr.left = tmp.right
        tmp.right = curr
        node.right = tmp.left
        tmp.left = node
        tmp.parent = node.parent
        node.parent = tmp
        curr.parent = tmp
        if tmp.parent == None:
            self.root = tmp
        else:
            tmp.parent.right = tmp
        return tmp
    
    def leftRightRotate(self, node):
        curr = node.left
        tmp = curr.right
        curr.right = tmp.left
        tmp.left = curr
        node.left = tmp.right
        tmp.right = node
        tmp.parent = node.parent
        node.parent = tmp
        curr.parent = tmp
        if tmp.parent == None:
            self.root = tmp
        else:
            tmp.parent.left = tmp
        return tmp
        
    
    def _height(self, node):
        if node == None:
            return -1 
        left = self._height(node.left)
        right = self._height(node.right)
        return max(left, right) + 1
        
    def height(self, node):
        if node == None:
            return -1
        return self._height(node)



    # In this function below we dont need a parent node. Page 244 
    def checkHeight(self, node):
        if node == None:
            return 0
        left = self.checkHeight(node.left)
        if left == -1:
            return -1 
        right = self.checkHeight(node.right)
        if right == -1:
            return -1 
        heightDiff = left - right
        if abs(heightDiff) > 1:
            return -1
        return max(left, right) + 1

    def  breadth_traversal(self):
        q = []
        q.append(self.root)
        lst = []
        while len(q):
            node = q.pop(0)
            lst.append(node.element)
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        return lst
        
b = BinarySearchTree()
b.add(43)
b.add(18)
b.add(22)
b.add(9)
b.add(21)
b.add(6)
b.add(8)
b.add(20)
b.add(63)
b.add(50)
b.add(62)
b.add(51)
# b.add(100)
print(b.breadth_traversal())
     