direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

ROTTEN, FRESH, EMPTY = 2, 1, 0

def OrangesRotting(matrix):
    rowLen, colLen = len(matrix), len(matrix[0])
    if rowLen == 0:
        return 0
    queue = []
    freshOranges = 0

    for row in range(rowLen):
        for col in range(colLen):
            if matrix[row][col] == ROTTEN:
                queue.append([row, col])
            if matrix[row][col] == FRESH:
                freshOranges += 1
    currentQueueSize = len(queue)
    minutes = 0
    while len(queue):
        if currentQueueSize == 0:
            minutes += 1
            currentQueueSize = len(queue)

        currentOrange = queue.pop(0)
        currentQueueSize -= 1
        row = currentOrange[0]
        col = currentOrange[1]

        for i in range(len(direction)):
            currentDir = direction[i]
            nextRow = currentDir[i] + row
            nextCol = currentDir[i] + col

            if nextRow < 0 or nextRow >= rowLen or nextCol < 0 or nextCol >= colLen:
                continue
            if matrix[nextRow][nextCol] == FRESH:
                matrix[nextRow][nextCol] = 2
                freshOranges -= 1
                queue.append([nextRow, nextCol])

    if freshOranges > 0:
        return -1
    return minutes

