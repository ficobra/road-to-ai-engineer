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

array_b = np.array([15, 42, 8, 73, 23, 56, 91, 4, 38, 67])
print(array_b[array_b > 40])
print(array_b[array_b % 2 == 0])
print(array_b[(array_b > 20) & (array_b < 70)])