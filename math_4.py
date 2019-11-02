# Решите аналитически и потом численно (в программе) уравнение, зависящее от параметра а:
# sin(а*x)=0
# при условии: 0.01<a<0.02, 100<х<500.
# Т.е. надо найти решение х как функцию параметра а - построить график x=x(а).
# Если численным методом не получается найти все ветви решения x(а), то отыщите хотя бы одну.


import numpy as np
import matplotlib.pyplot as plt
import scipy

a = np.arange(0.01, 0.02, 0.001)
x = np.arange(100, 500, 0.1)
y = []

for i in a:
    for e in x:
        y.append(np.sin(np.dot(e, i)))
        if np.sin(np.dot(e, i)) == 0:
            print(e, i)

# def func(y):
#     for i in a:
#         for e in x:
#     return np.sin(np.dot(e, i))

plt.plot(y)
plt.show(block=True)




