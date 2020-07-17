class Matrix:
    def __init__(self):
        self.matrix = []
        
    def insert(self, column):
        self.matrix.append(column)
        return self.matrix
        
    def create_matrix(self, row, column):
        for i in range(row):
            self.matrix.append([0. for _ in range(column)])
        return self.matrix
        
    def uniform_distrbution(self):
        probability = 1 / (len(self.matrix) * len(self.matrix[0]))
        n = len(self.matrix[0])
        for column in self.matrix:
            i = 0
            while i < n:
                column[i] = probability
                i += 1
        return self.matrix
    
           
matrix = Matrix()
matrix.create_matrix(3, 3)
# matrix.uniform_distrbution()