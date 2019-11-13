import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

# 1. Решите линейную систему:
A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
print(np.linalg.solve(A, B))

# 2. Найдите псевдорешение:

C = ([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]])
D = ([1, 7, 12, 7, 15])
print(np.linalg.lstsq(C, D))
a = np.dot(C, [1.13919353, -0.90498444, -0.9009803])
print(np.linalg.norm(a))

# 3. Сколько решений имеет линейная система:
E = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
F = np.array([12, 2, 1])
# print(np.linalg.solve(E, F))

# 4. Вычислите LU-разложение матрицы:
G = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(G)
print(P)
print(L)
print(U)
H = np.array([6, 39, 105])
print(np.linalg.solve(G, H))



