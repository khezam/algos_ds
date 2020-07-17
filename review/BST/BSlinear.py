class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, element):
        new_node = Node(element)
        if self.root == None:
            self.root = new_node
            return 
        return self._insert(self.root, new_node)
                
    
    def _insert(self, node, new_node):
        while node:
            if node.element < new_node.element:
                if node.right == None:
                    node.right = new_node
                    return 
                else:
                    node = node.right
            else:
                if node.left == None:
                    node.left = new_node
                    return 
                else:
                    node = node.left
                    
    def search(self, target):
        if not self.root:
            return 
        if self.root.element == target:
            return True 
        return self._search(self.root, target)
        
    def _search(self, node, target):
        while node:
            if node.element == target:
                return True
            if node.element < target:
                node = node.right
            else:
                node = node.left
        return False
        
    def delete(self, target):
        if not self.root:
            return "Tree is empty"
        return self._delete(self.root, target, None)
        
    def _successor(self, curr):
        tmp  = curr
        curr = curr.right
        while curr.left:
            if curr.left.left == None:
                successor = curr.left.element
                curr.left = None
                return successor
            curr = curr.left
        successor = curr.element
        tmp.right = None
        return successor

    # Delete itervatly done by me!    
    def _delete(self, node, target, parent):
        while node:
            if node.element == target:
                if not node.left and not node.right:
                    if parent.left == node:
                        parent.left = None
                        return
                    else:
                        parent.right = None
                        return
                if node.left == None or node.right == None:
                    if node.left:
                        parent.left = node.left
                        return parent
                    else:
                        parent.right = node.right
                        return parent
                if node.left and node.right:
                    node.element = self._successor(node)
                    return node
                        
            if node.element < target:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left
        return "Not found"


    # Done by me iteravley
    def _preOrder(self, node):
        # Explor where we are by visiting the node
        visited = set()
        visited.add(node.element)
        # Add it to the stack
        stack = [node]
        len_of_stack = len(stack)
        lst = [node.element]
        while len_of_stack:
            # Explor the neighbors
            if node.left and node.left.element not in visited:
                node = node.left
                visited.add(node.element)
                stack.append(node)
                lst.append(node.element)
                len_of_stack += 1
            elif node.right and node.right.element not in visited:
                node = node.right
                visited.add(node.element)
                stack.append(node)
                lst.append(node.element)
                len_of_stack += 1
            else:
                stack.pop()
                len_of_stack -= 1
                if len_of_stack:
                    node = stack[len_of_stack-1]
                else:   
                    return lst

    # better version done by me and I know how i did it 
    def _preOrder(self, node):
        stack = [node]
        lst = [node.element]
        while len(stack):
            if node and node.left:
                node = node.left
                stack.append(node)
                lst.append(node.element)
            else:
                node = stack.pop()
                node = node.right
                if node:
                    stack.append(node)
                    lst.append(node.element)
        return lst


    # I'm not sure how did it but it works! 
    def postOrder(self):
        return self._postOrder(self.root)
        
    def _postOrder(self, node):
        visited = set()
        stack = [node]
        lst = []
        while len(stack):
            if node and node.left and node.left not in visited:
                node = node.left
                stack.append(node)
            elif node and node.right and node.right not in visited:
                node = node.right
                stack.append(node)
            else:
                if node and node not in visited:
                    visited.add(node)
                    lst.append(node.element)
                visited.add(stack.pop())
                if len(stack):
                    node = stack[len(stack)-1]
                else:
                    visited = None
                    return lst

    # I'm not sure how did it but it works! 
    def inOrde(self):
        return self._inOrder(self.root)
        
    def _inOrder(self, node):
        visited = set()
        stack = [node]
        lst = []
        while node:
            if node and node.left and node.left not in visited:
                node = node.left
                stack.append(node)
            elif node and node.right and node.right not in visited:
                node = node.right
                stack.append(node)
            else:
                if node and node not in visited:
                    tmp = stack.pop()
                    visited.add(tmp)
                    lst.append(tmp.element)
                if len(stack):
                    node = stack.pop()
                    visited.add(node)
                    lst.append(node.element)
                else:
                    visited = None
                    return lst


    # Done by Tushar video
    def inOrder(self):
        return self._inOrder(self.root)
        
    def _inOrder(self, node):
        stack = []
        lst = []
        while True:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0:
                    return
                node = stack.pop()
                lst.append(node.element)
                node = node.right

    # done by me 
    def _inOrder(self, node):
        stack = [node]
        lst = []
        while len(stack):
            if node:
                node = node.left
                stack.append(node)
            else:
                node = stack.pop()
                if node:
                    lst.append(node.element)
                    node = node.right
                    stack.append(node)
        return lst

    # done by me just the way recursive version works and i like it 
    def _inOrder(self, node):
        stack = [node]
        lst = []
        while len(stack):
            if node == None:
                node = stack.pop()
                if not stack:
                    return lst
                lst.append(node.element)
                node = node.right
            else:
                stack.append(node)
                node = node.left
        return lst

    def inser_arr(self, arr):
        self.root = self._inser_arr(arr, 0, len(arr)-1)
        return self.root
        
    def _inser_arr(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(arr[mid])
        node.left = self._inser_arr(arr, start, mid - 1)
        node.right = self._inser_arr(arr, mid + 1, end)
        return node


    def check_balance(self):
        return self._checkB(self.root)
        
    def _checkB(self, node):
        if node == None:
            return 0
        left = self._checkB(node.left)
        if left == -1:
            return -1 
        right = self._checkB(node.right)
        if right == -1:
            return -1 
        if abs(left - right) > 1:
            return -1 
        return max(left, right) + 1
    
        
                    

b = BST()
for item in [100, 20, 10, 40, 5, 15, 35, 1, 50, 200, 150, 250,120, 180, 220, 300]:
    b.insert(item)
  