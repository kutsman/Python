import numpy as np


class Matrix:

    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return '\n'.join(map(str, self.arr))

    def __add__(self, other):
        return np.array(self.arr) + np.array(other.arr)


array_1 = Matrix([[1, 2, 6], [1, 5, 4], [7, 10, 1]])
array_2 = Matrix([[5, 0, 3], [1, 2, 8], [2, 5, 4]])
print(f"Матрица А:\n{array_1}")
print(f"Матрица B:\n{array_2}")
sum_arr = array_1 + array_2
print(f"Матрица A+B:\n{sum_arr}")
