import numpy
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

# Решите систему уравнений:
# y = x2 – 1
# exp(x) + x∙(1 – y) = 1
#
#
# Решите систему уравнений и неравенств:
# y = x2 – 1
# exp(x) + x∙(1 – y) > 1

x = numpy.linspace(0, 10, 500)


def func(q):
    x, y = q
    return y - x ** 2 + 1, numpy.exp(x) + x * (1 - y) - 1


x1, y1 = fsolve(func, (1, 10))
print("x равно ", x1, " y равно ", y1)


def func_1(m):
    x2, y2 = m
    return y2 - x ** 2 + 1, numpy.exp(x2) + x2 * (1 - y2) - 1


x2, y2 = fsolve(func, (4, 20))
print("x меньше ", x2, " y меньше ", y2)
