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
    
    def size(self, node):
        if node == None:
            return 0
        left = self.size(node.left)
        right = self.size(node.right)
        return (left+right) + 1
    
    def _minValue(self, node):
        if node.left == None:
            return node.element
        return self._minValue(node.left)
    
    def minValue(self):
        if self.root:
            if self.root.left:
                return self._minValue(self.root)
            return self.root.element
        return "Empty Tree"
    
    def _maxValue(self, node):
        if node.right == None:
            return node.element
        return self._maxValue(node.right)
        
    def maxValue(self):
        if self.root:
            if self.root.right:
                return self._maxValue(self.root)
            return self.root.element
        return "Emptyy Tree"


    # This approach is correct but it causes the tree to be unbalanced    
    def unbalanceSolution(self, nodeLeft, nodeRight):
        curr = nodeRight
        while curr.left:
            curr = curr.left
        curr.left = nodeLeft
        return nodeRight
    
    # This function does not cause thr tree be balanced
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
                    # If the right subtree has only one sucessor node   
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


    # This function belows checks if the tree is a binary search tree but WRONG
    # Done by 
    def is_BS(self, node, successor):
        if node == None:
            return None
        left = self.is_BS(node.left, node)
        right = self.is_BS(node.right, successor)
        if left == None and right == None:
            return node
        if left and left.element >= node.element:
            return False
        if right and right.element <= node.element or successor and right.element >= successor.element:
            return False
        return node



    # pre-order iterive way done by me 
    def preOrder(self, node):
        if node == None:
            return None
        table = set()
        table.add(node.element)
        lst = list()
        lst.append(node.element)
        stack = [node]
        while len(stack):
            if node.left and node.left.element not in table:
                node = node.left
                stack.append(node)
                lst.append(node.element)
                table.add(node.element)
            elif node.right and node.right.element not in table:
                node = node.right
                stack.append(node)
                lst.append(node.element)
                table.add(node.element)
            else:
                stack.pop()
                if len(stack):
                    node = stack[len(stack)-1]
                else:
                    return lst


    # PreOrder iteriave way 
    def preOrderIter(self, node):
        if node == None:
            return None
        lst = list()
        stack = [node]
        while len(stack):
            node = stack.pop()
            lst.append(node.element)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    # insertion iterave from Udacity
    def insert(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping

    # BFS algorithm
    # The reper function below and this function go together
    def bfs(tree):
        q = Queue()
        visit_order = list()
        node = tree.get_root()
        q.enq(node)
        while len(q):
            node = q.deq()
            visit_order.append(node.value)
            if node.has_left_child():
                q.enq(node.right)
            if node.has_right_child():
                q.enq(node.right)
        return visit_order

    # BFS to represent nodes with values or None into a list
    # from Udacity
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("None", level))
                continue
            visit_order.append( (node.value, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
        s = ""
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s +=  " " + str(node)
            else:
                s +=  " " + str(node)
                previous_level = level

        return s



    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1


    # Search iterave by Udacity
    def search(self,value):
        node = self.get_root()
        s_node = Node(value)
        while(True):
            comparison = self.compare(node,s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
        
        
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
# b.remove(60)



        