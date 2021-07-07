directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def traverseDFS(matrix):
    seen = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    values = []
    dfs(matrix, 0, 0, seen, values)

    return values

def dfs(matrix, row, col, seen, values):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]:
        return
    values.append(matrix[row][col])
    seen[row][col] = True

    for i in range(len(directions)):
        currentDir = directions[i]
        dfs(matrix, row+currentDir[0], col+currentDir[1], seen, values)

print(traverseDFS([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20]]))