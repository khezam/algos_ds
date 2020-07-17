# Done by me


class Node:
    def __init__(self, element):
        self.element = element
        self.next = []
        

class Graph:
    def __init__(self, weight=4):
        self.graph = [None for _ in range(weight)]
        self.totalDeg = 0
        self.size = -1
        
    def _add(self, element1, element2):
        node1 = Node(element1)
        node2 = Node(element2)
        if self.size == -1:
            self.graph[self.size+1] = node1
            node1.next = [element2]
            self.totalDeg += 1
            self.size += 1
            self.graph[self.size+1] = node2
            node2.next = [element1]
            self.totalDeg += 1
            self.size += 1
            return self.graph
            
    def add(self, element1, element2):
        if self.size == -1:
            return self._add(element1, element2)
        i = 0
        nodeFlag1 = False
        nodeFlag2 = False
        while i < len(self.graph):
            if self.graph[i] and self.graph[i].element == element1 and self.graph[i] != None:
                node = self.graph[i]
                node.next.append(element2)
                nodeFlag1 = True
                self.totalDeg += 1
                self.size += 1
            elif self.graph[i] and self.graph[i].element == element2 and self.graph[i] != None:
                node = self.graph[i]
                node.next.append(element1)
                nodeFlag2 = True
                self.totalDeg += 1
                self.size += 1
            elif self.graph[i] == None:
                break
            i += 1
        if nodeFlag1 == False and nodeFlag2 == False:
            return self._add(element1, element2)
        if not nodeFlag1:
            new_node = Node(element1)
            new_node.next.append(element2)
            self.graph[i] = new_node
        if not nodeFlag2:
            new_node = Node(element2)
            new_node.next.append(element1)
            self.graph[i] = new_node
        return self.graph
            
            
            

        
g = Graph(10)
g.add('SF', 'LA')
g.add('LA', 'SD')
g.add('NY', 'LA')
g.add('SD', 'NY')
g.add('LV', 'SF')

