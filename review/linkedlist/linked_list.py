class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def preappend(self, element):
        if not self.head:
            self.append(element)
        else:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        return self
        
        
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1
        return self.head
        
    def pop(self):
        if self.head:
            node = self.head
            while node.next.next:
                node = node.next
            self.tail = node
            node.next = None
            self.count -= 1
            return self.head
        return "Stack is empty"
        
    def dequeue(self):
        if self.head:
            self.head = self.head.next
            self.count -= 1
            return self.head
        return "Queue is empty"
        
    def _search(self, element):
        if self.head:
            node = self.head
            while node and node.element != element:
                prev = node
                node = node.next
            if not node:
                return 
            return prev
        return
    
    def search(self, element):
        prev = self._search(element)
        if prev:
            return True
        return 
        
    def delete(self, element):
        if self.head:
            prev = self._search(element)
            if prev:
                if prev.next.next:
                    prev.next = prev.next.next
                    self.count -= 1
                    return self.head
                self.tail = prev
                prev.next = None
                self.count -= 1
                return self.head
            return "Not found"
        return "No nodes avail"

    def insert(self, index, element):
        if self.head:
            index = index - 1
            if index <= 1:
                return self.preappend(element)
            elif index > 1 and index < self.count:
                new_node = Node(element)
                node = self.head
                i = 1
                while i < index:
                    i += 1
                    node = node.next 
                new_node.next = node.next
                node.next = new_node
                self.count += 1
                return self.head
            else:
                return self.append(element)
        return "No nodes avai"

    def delByIndex(self, node, index):
        if node == None or index <= 0:
            return False
        index = index - 1
        if index == 0:
            if node.next:
                node = node.next
                self.head = node
                return
            node = self.head = None
            return 
        i = 1
        while node and i < index:
            node = node.next
            i += 1
        if node and node.next and i == index:
            if node.next.next:
                node.next = node.next.next
                return 
            node.next = None
            return
        return "Index is large"


    def deleteByIndex(self, index):
        if self.head == None:
            return self.empty
        if index <= 0:
            return "No index less than 0"
        if index == 1:
            self.head = self.head.next
            return 
        index = index - 1
        i = 1
        node = self.head
        while node and i < index:
            node = node.next
            i += 1
        if i == index and node.next:
            if node.next.next:
                node.next = node.next.next
                return
            node.next = None
            return
        return


    def insertByIndex(self, node, index, element):
        if node == None or index <= 0 :
            return False
        index = index - 1
        new_node = self.Node(element)
        if index == 0:
            new_node.next = node
            self.head = new_node
            return 
        i = 1 
        while node.next and i < index:
            i += 1
            node = node.next
        if i < index:
            return "index is larger than length"
        if node.next:
            new_node.next = node.next 
            node.next = new_node
            return
        node.next = new_node
        return

    # Better version than function above
    def insertByIndex(self, node, index, element):
        if node == None or index <= 0 :
            return False
        index = index - 1
        new_node = self.Node(element)
        if index == 0:
            new_node.next = node
            self.head = new_node
            return 
        i = 1 
        while node.next and i < index:
            i += 1
            node = node.next
        new_node.next = node.next 
        node.next = new_node
        return

        
        
    def reverse(self, node):
        if not node or not node.next:
            return node
        curr = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return curr

    def reverse(self, node):
        if not node or not node.next:
            return node
        curr = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return curr


    # reversing iteravily usung stack done by me
    def reverse(self):
        node = self.head 
        stack = []
        while node:
            stack.append(node)
            node = node.next
        self.head = None
        n = len(stack) - 1
        tail = None
        while n > -1:
            if self.head == None:
                self.head = stack[n]
            else:
                tail.next = stack[n]
            tail = stack[n]
            tail.next = None
            n -= 1
        stack = tail = None
        return self.head


    # I edited some stuff from the original function right above done by me 
    def reverse(self):
        node = self.head 
        stack = []
        count = -1
        while node:
            stack.append(node)
            node = node.next
            count += 1
        self.head = None
        while count > -1:
            if self.head == None:
                self.head = stack[count]
            else:
                node.next = stack[count]
            node = stack[count]
            node.next = None
            stack[count] = None
            count -= 1
        stack = node = None
        return self.head

    # Reversing without using stack
    def reverse(self, node):
        if node == None:
            return node
        prev = None
        curr = node
        while node:
            node = node.next
            curr.next = prev
            prev = curr
            curr = node
        self.head = prev
        return

    # Reverse by me 
    def reverse(self, node):
        if node == None:
            return node
        curr = node
        node = node.next
        curr.next = None
        while node:
            prev = curr
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
        self.head = prev
        return

    # Delete duplicates from linkedlist done by me 
    def find_duplicate(self, curr):
        if curr == None:
            return curr
        prev = None
        hash = set()
        while curr:
            if curr.element not in hash:
                hash.add(curr.element)
                prev = curr
                curr = curr.next
            else:
                curr = curr.next
                prev.next = curr
        return self.head

    def findDup(self, node):
        if node == None:
            return node
        while node:
            curr = node 
            while curr.next:
                if curr.next.element == node.element:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            node = node.next
        return self.head

    # Find duplicates without using extra space done by me 
    def findDup(self, node):
        if node == None:
            return node
        while node:
            curr = node 
            while curr and curr.next:
                if curr.next.element == node.element:
                    if curr.next.next:
                        curr.next = curr.next.next
                    else:
                        curr.next = None
                else:
                    curr = curr.next
            node = node.next
        return self.head


    # Done by me 
    def is_palindrome(self, node):
        if node == None or node.next == None:
            return node
        stack = []
        n = -1 
        curr = node
        while curr:
            stack.append(curr)
            curr = curr.next 
            n += 1
        while node != stack[n]:
            if node.element != stack[n].element:
                return False
            stack[n] = None
            n -= 1
            node = node.next
        return True
    
        
    def cyrclePos(self, index):
        i = 0
        node = self.head
        while i < self.count and i != index:
            i += 1
            node = node.next
        self.tail.next = node
        self.tail = None
        return self.head

    # Done by me 
    def isLoop(self, node):
        if node == None or node.next == None:
            return node
        hash = set()
        while node and node not in hash:
            hash.add(node)
            node = node.next
        return node
        
    def cyrcle(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
def intersection(headA, headB):
    nodeA = headA
    nodeB = headB
    if not nodeA or not nodeA.next:
        return False
    if not nodeB or not nodeB.next:
        return False
        
    while nodeA != nodeB:
        if nodeA != nodeB and nodeA.next == None and nodeB.next == None:
            return False
        if nodeA.next == nodeB.next:
            return nodeA.next
        if not nodeA.next:
            nodeA = headA
        if not nodeB.next:
            nodeB = headB
        nodeA = nodeA.next
        nodeB = nodeB.next
    return nodeA



    def delete(self, target):
        if not self.head:
            return
        if self.head.element == target:
            self.head = self.head.next
        node = self.head 
        while node:
            if node.element == target and prev:
                prev.next = node.next 
                return self.head
            prev = node 
            node = node.next 
        return "Not foud"
        
    def insert(self, element, target):
        if not self.head:
            return
        new_node = Node(element)
        if self.head.element == target:
            new_node.next = self.head.next
            self.head = new_node
            return
        node = self.head 
        while node:
            if node.element == target:
                new_node.next = node
                prev.next = new_node
                return 
            prev = node
            node = node.next 
        return

    # def cyrcle(self):
    #     i = self.head
    #     if not i:
    #         return
    #     if not i.next:
    #         return i
    #     while i and i.next:
    #         if i.next == self.head:
    #             return i.next
    #         j = self.head
    #         while j.next != i.next and j != i and j != i.next:
    #             j = j.next
    #         if j == i:
    #             i = i.next
    #             j = self.head
    #         elif j.next == i.next or j == i.next:
    #             return i.next
    #     return "It's not cyricular"


            
l = LinkedList()
l.append(3)
l.append(2)
l.append(0)
l.append(-4)
l.append(19)
l.append(6)
l.append(-9)

print(l.count)
l.cyrclePos(l.coun)
print(l.cyrcle().element)
