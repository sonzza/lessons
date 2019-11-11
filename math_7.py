import numpy as np
import matplotlib.pyplot as plt

# 1. Решите линейную систему:
A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
print(np.linalg.solve(A, B))

# 2. Найдите псевдорешение:

C = ([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]])
D = ([1, 7, 12, 7, 15])
print(np.linalg.lstsq(C, D))

E = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
F = np.array([12, 2, 48])


print(np.linalg.lstsq(E, F))
# 5. Найдите нормальное псевдорешение недоопределенной системы:

G = np.array([[1, 2, -1], [8, -5, 2]])
H = np.array([1, 12])
def A():
    return (np)
x = np.linspace(-10, 100, 200)
plt.plot()