class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            return 
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        return
    
    def merge(self, midPoint, node):
        while node.next:
            node = node.next
        node.next = midPoint
    
    def length(self, node):
        n = 1
        while node.next:
            n += 1
            node = node.next
        return node, n
        
    def getDiff(self, node, diff):
        while diff > 0 and node:
            node = node.next
            diff -= 1
        return node
    
    def intersection(self, node1, node2):
        if node1 == None or node2 == None:
            return None
            
        tail1, lenNode1 = self.length(node1)
        tail2, lenNode2 = self.length(node2)
        if tail1 != tail2:
            return None
         
        tail1 = None
        tail2 = None
        shorter = None
        longer = None
        
        diff = abs(lenNode1 - lenNode2)
        if lenNode1 > lenNode2:
            longer = self.getDiff(node1, diff)
            shorter = node2
        elif lenNode2 > lenNode1:
            longer = self.getDiff(node2, diff)
            shorter = node1
        else:
            longer = node1
            shorter = node2
        
        while longer != shorter:
            longer = longer.next
            shorter = shorter.next
        return longer
    
            
    
    
# first = LinkedList()
# first.add(3)
# first.add(1)
# first.add(5)
# first.add(9)


# midNode = LinkedList()
# midNode.add(7)
# midNode.add(2)
# midNode.add(1)
# midNode = midNode.head


# second = LinkedList()
# second.add(4)
# second.add(6)
# second.add(4)
# second.add(6)
# second.add(4)
# second.add(6)
# first.merge(midNode, first.head)
# second.merge(midNode, second.head)
# midNode = None

# LinkedList().intersection(first.head, second.head)
               
               
               
                