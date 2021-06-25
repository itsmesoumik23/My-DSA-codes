class Hamiltonian(object):
    def __init__(self, adjacencyMatrix):
        self.adjacencyMatrix = adjacencyMatrix
        self.n = len(self.adjacencyMatrix)
        self.path = [0]     # initialised with starting index

    def Hamiltonian_path(self):
        if self.solve(1):
            self.show_hamiltonian_path()
        else:
            print("No Possisble Path...")

    def solve(self, position):
        # BASE CASE
        if position == self.n:
            return True
        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                self.path.append(vertex_index)
                if self.solve(position+1):
                    return True
                else:   # backtrack
                    self.path.pop()
        return False

    def is_feasible(self, vertex_index, position):
        if self.adjacencyMatrix[self.path[position-1]][vertex_index] == 0:
            return False

        for i in range(position):
            if self.path[i] == vertex_index:
                return False
        return True

    def show_hamiltonian_path(self):
        print(self.path)

if __name__ == "__main__":
    h = Hamiltonian([[0, 1, 0], [1, 0, 1], [1, 1, 0]])
    h.Hamiltonian_path()