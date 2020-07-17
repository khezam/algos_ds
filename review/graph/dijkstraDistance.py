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
                    elif new_dist < dis_so_far[node.element]:
                        dis_so_far[node.element] = new_dist
                    path[node.element] = w
                node = node.next
        return final_dist


    def dijkstra(self, start_node, end_node):
        dis_so_far = {start_node:0}
        final_dist = {}
        path = {start_node: None}
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
                    elif new_dist < dis_so_far[node.element]:
                        dis_so_far[node.element] = new_dist
                    path[node.element] = w
                node = node.next
        return final_dist
        

# g = Graph()
# g.add('A', 'C', 3)
# g.add('A', 'D', 4)
# g.add('A', 'B', 15)
# g.add('C', 'B', 10)
# g.add('D', 'B', 9)
# g.add('D', 'F', 7)
# g.add('D', 'E', 3)
# g.add('E', 'F', 5)
# g.add('E', 'G', 1)
# g.add('G', 'F', 2)
# g.add('F', 'B', 1)

# result = g.dijkstra('A', 'B')





#------------------------
#BFS
class Graph(object):

    def dfs_helper(self, start_node):
        """The helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        REQUIRES: self._clear_visited() to be called before
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """
        ret_list = [start_node.value]
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                     if e.node_to.value != start_node.value]
        for edge in edges_out:
            if not edge.node_to.visited:
                ret_list.extend(self.dfs_helper(edge.node_to))
        return ret_list

    def bfs(self, start_node_num):
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = []
        # Your code here
        queue = [node]
        node.visited = True
        def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
        def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))
        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            for e in node.edges:
                if unvisited_outgoing_edge(node, e):
                    enqueue(e.node_to)
        return ret_list
        