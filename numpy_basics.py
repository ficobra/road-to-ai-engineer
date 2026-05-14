import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix.shape)
print(matrix.sum())
print(matrix.mean())
print(2 * matrix)

array_a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(array_a[1, 2])
print(array_a[1, :])
print(array_a[:, 2])
print(array_a[0:2, 1:])