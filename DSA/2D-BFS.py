directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def traverseBFS(matrix):
    seen = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    values = []
    queue = [[0, 0]]
    while len(queue):
        currentPos = queue.pop(0)
        row = currentPos[0]
        col = currentPos[1]
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
            continue
        seen[row][col] = True
        values.append(matrix[row][col])

        for i in range(len(directions)):
            currentDir = directions[i]
            queue.append([row+currentDir[0], col+currentDir[1]])
    return values

print(traverseBFS([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20]]))