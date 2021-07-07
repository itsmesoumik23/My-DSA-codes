import heapq
class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        # the node where we came from
        self.predecessor = None
        # to store the children
        self.adjList = []
        # shortest path from start vertex
        self.min_distance = float('inf')

    # this is how python compare objects
    # after inserting the objects into the heap
    # heap can compare given objects

    def __lt__(self, other):
        return self.min_distance < other.min_distance

class Dijkstra(object):
    def __init__(self):
        self.heap = []

    def calculate(self):
        # initialise vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        # iterate until heap is empty
        while self.heap:

            # pop the vertex with lowest min distance parameter
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            # we have to consider the neighbours
            for edge in actual_vertex.adjList:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + weight

                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    # update the heap
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        print(f"Shortest path to vertex is : {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(f"{actual_vertex.name} ")
            actual_vertex = actual_vertex.predecessor
