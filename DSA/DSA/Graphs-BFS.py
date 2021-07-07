# we will traverse through adjacency list

def traverseBFS(graph):
    queue = [0]
    values = []
    seen = {}
    while len(queue):
        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex] = True
        connections = graph[vertex]
        for i in range(len(connections)):
            connection = connections[i]
            if not seen[connection]:
                queue.append(connection)
