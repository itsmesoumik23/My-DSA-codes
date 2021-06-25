class MazeProblem(object):
    def __init__(self, mazeTable):
        self.mazeTable = mazeTable
        self.mazeSize = len(mazeTable)
        self.solutionTable = [[0] * self.mazeSize for i in range(self.mazeSize)]

    def solveMaze(self):
        if self.solve(0, 0):
            self.showResult()
        else:
            print("No path available...")

    def solve(self, x, y):
        if self.isFinished(x, y):
            return True
        if self.isValid(x, y):
            self.solutionTable[x][y] = 1

            if self.solve(x+1, y):
                return True
            if self.solve(x, y+1):
                return True

            # no feasible next path: so backtrack
            self.solutionTable[x][y] = 0
        return False

    def isFinished(self, x, y):
        if x == self.mazeSize-1 and y == self.mazeSize-1:
            self.solutionTable[x][y] = 1
            return True
        return False

    def isValid(self, x, y):
        if x < 0 or x >= self.mazeSize:
            return False
        if y < 0 or y >= self.mazeSize:
            return False
        if self.mazeTable[x][y] == 0:
            return False
        return True

    def showResult(self):
        for i in range(self.mazeSize):
            for j in range(self.mazeSize):
                if self.solutionTable[i][j] == 0:
                    print("_", end=" ")
                else:
                    print("S", end=" ")
            print()

if __name__ == "__main__":
    maze = MazeProblem([[1, 1, 1, 1, 1],
                        [1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 0, 1]])
    maze.solveMaze()