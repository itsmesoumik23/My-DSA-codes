directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def numberOfIslands(matrix):
    if len(matrix) == 0:
        return 0
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                counter += 1
                matrix[row][col] = 0
                queue = []
                queue.append([row, col])

                while len(queue):
                    currentPos = queue.pop(0)
                    currentRow = currentPos[0]
                    currentCol = currentPos[1]

                    for i in range(len(directions)):
                        currentDir = directions[i]
                        nextRow = currentRow + currentDir[0]
                        nextCol = currentCol + currentDir[1]

                        if nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[0]):
                            continue
                        if matrix[nextRow][nextCol] == 1:
                            queue.append([nextRow, nextCol])
                            matrix[nextRow][nextCol] = 0

    return counter
