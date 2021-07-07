class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.predecessor = None
        self.min_distance = float('inf')

class BellmanFord(object):
    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0

        # it makes V-1 iterations so O(V-1)
        for _ in range(len(self.vertex_list)-1):
            # we consider all the edges
            # O(E)
            for edge in self.edge_list:
                u = edge.start_vertex
                v = edge.target_vertex

                dist = u.min_distance + edge.weight
                if dist < v.min_distance:
                    v.min_distance = dist
                    v.predecessor = u
        # till so far running time O(V-1)xO(E)

        # extra 1 iteration to check cycles
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("Negative cycle detected")
                return

    def check_cycle(self, edge):
        # if total cost decreases after 1 iteration
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, vertex):
        if not self.has_cycle:
            print(f"Shortest path with value : {vertex.min_distance}")
            node = vertex
            while node is not None:
                print(node)
                node = node.predecessor
        else:
            print("Negative cycles detected...")