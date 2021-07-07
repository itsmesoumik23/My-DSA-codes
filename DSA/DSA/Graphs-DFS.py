adjacencyList = [[1, 3],
                 [0],
                 [3, 8],
                 [0, 4, 5, 2],
                 [3, 6],
                 [3],
                 [4, 7],
                 [6],
                 [2]]


# each index is vertx
# 1-D list items are connected vertices
# 0th item is [1, 3] means vertex "0" is connected with vertex "1" and "3"

def traverseDFS(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True
    connections = graph[vertex]  # 1D list item
    for i in range(len(connections)):
        connection = connections[i]  # items of 1D array
        if not seen[connection]:
            traverseDFS(connection, graph, values, seen)
    