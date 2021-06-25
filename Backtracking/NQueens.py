class QueensProblem(object):

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def solve_n_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("No Solution...")

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print("_", end=" ")
            print()

    def solve(self, col):
        # base case if we have solved the problem
        if col == self.n:
            return True

        for row in range(self.n):
            if self.validPlace(row, col):
                self.chess_table[row][col] = 1
                if self.solve(col+1):
                    return True
                else:   # backtrack
                    self.chess_table[row][col] = 0
        return False

    def validPlace(self, row, col):
        # check rows
        for i in range(self.n):
            if self.chess_table[row][i] == 1:
                return False

        # check diagonals from top left to bottom right
        j = col
        for i in range(row, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        # check diagonals from top right to bottom left
        j = col
        for i in range(row, self.n):
            if j < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        return True

if __name__ == "__main__":
    queen = QueensProblem(4)
    queen.solve_n_queens()
