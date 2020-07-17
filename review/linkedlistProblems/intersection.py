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
    
    
    # Using a simple hash table on the node's reffrences 
    def nodeIntersect(self, node1, node2):
        table = set()
        while node1:
            if node1 in table:
                return node1
            table.add(node1)
            node1 = node1.next
        
        while node2:
            if node2 in table:
                return node2
            table.add(node2)
            node2 = node2.next
        
        return 
            
    
    
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

# first.merge(midNode, first.head)
# second.merge(midNode, second.head)
# midNode = None

# LinkedList().nodeIntersect(first.head, second.head)
               
               
               
                