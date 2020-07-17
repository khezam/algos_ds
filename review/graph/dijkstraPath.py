class GraphNode:
    def __init__(self, element, weight):
        self.element = element
        self.weight = weight
        self.next = None
        
class Graph:
    def __init__(self):
        self.graph = {}
    
    
    def traverse(self, node):
        while node.next:
            node = node.next
        return node    
        
    def add(self, node1, node2, weight):
        new_node1 = GraphNode(node1, weight)
        new_node2 = GraphNode(node2, weight)
        if node1 not in self.graph:
            self.graph[node1] = new_node2
        else:
            curr = self.traverse(self.graph[node1])
            curr.next = new_node2
            
        if node2 not in self.graph:
            self.graph[node2] = new_node1
        else:
            curr = self.traverse(self.graph[node2])
            curr.next = new_node1
        return self.graph
        
                    
    def shortest_dist_node(self, dist):
        best_node = 'undefined'
        best_value = 100000
        for v in dist:
            if dist[v] < best_value:
                (best_node, best_value) = (v, dist[v])
        return best_node
    
    
    
    def dijkstra(self, start_node, end_node):
        dis_so_far = {start_node:0}
        final_dist = {}
        path = {start_node: None}
        path_to_node = {start_node:[start_node]}
        while len(final_dist) < len(self.graph):
            w = self.shortest_dist_node(dis_so_far)
            final_dist[w] = dis_so_far[w]
            del dis_so_far[w]
            node = self.graph[w]
            while node:
                if node.element not in final_dist:
                    new_dist = final_dist[w]+node.weight
                    if node.element not in dis_so_far:
                        dis_so_far[node.element] = new_dist
                        path[node.element] = w
                        path_to_node[node.element] = path_to_node[w] + [node.element]
                    elif new_dist < dis_so_far[node.element]:
                        dis_so_far[node.element] = new_dist
                        path[node.element] = w
                        path_to_node[node.element] = path_to_node[w] + [node.element]
                node = node.next
        return path_to_node
        
    
                    
                    
    
    
        
g = Graph()
g.add('A', 'B', 5)
g.add('A', 'D', 9)
g.add('A', 'E', 2)
g.add('C', 'D', 3)
g.add('D', 'F', 2)
g.add('E', 'F', 3)
g.add('B', 'C', 2)


result = g.dijkstra('A', 'C')

# Tushar youtube video example

