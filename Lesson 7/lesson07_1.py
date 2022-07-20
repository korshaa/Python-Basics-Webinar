import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        return '\n'.join('\t'.join(map(str, row)) for row in (np.array(self.matrix) + np.array(other.matrix)))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_1 + matrix_2)
