# 1. Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).

import numpy as np
import itertools
import matplotlib.pyplot as plt


def get_number():
    # input()
    x = np.random.randint(0, 37)
    # print("на рулетке выпало число ", x)
    return x


# 2.1 Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере
# рулетки или подбрасывания монетки.
a = get_number()
b = get_number()
n = 100


def get_P(n, a, b):
    l = 0
    m = 0
    for i in range(n):
        a1 = get_number()
        i += 1
        if a1 == a:
            l += 1
        if a1 == b:
            m += 1
    P = l / n + m / n
    print("Вероятность выпадения числа {}, и числа {} за {} рулеток равна {}".format(a, b, n, P))
    print("количество выпадений {} равно {}, количество выпадений {} равно {}".format(a, l, b, m))


get_P(n, a, b)

# 2.2 Сгенерируйте десять выборок случайных чисел х0, …, х9.
# и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.

number_list = np.random.randint(1, 11, 10)
random_sum = []
for i in range(10):
    for p in itertools.product(list(number_list), repeat=3):
        sum_p = p[0] + p[1] + p[2]
        random_sum.append(sum_p)
print(random_sum)
plt.hist(random_sum)
plt.show()

# 3.1 Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей (через биномиальное распределение)
# и сравните результаты.
# 3.2 Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности из n независимых испытаний, взяв другие значения n и k.


k3 = 0
n3 = 100000
a3 = np.random.randint(0, 2, n3)
b3 = np.random.randint(0, 2, n3)
c3 = np.random.randint(0, 2, n3)
d3 = np.random.randint(0, 2, n3)

x3 = a3 + b3 + c3 + d3
for i in range(0, n3):
    if x3[i] == 2:
        k3 += 1
print(k3, n3, k3 / n3)

# 4. Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты перестановок для других значений n и k

for p in itertools.permutations("012345", 3):
    print(''.join(p))

# 5. Дополните код расчетом коэффициента корреляции x и y по формуле

n5 = 100
r5 = 0.8
x5 = np.random.rand(n5)
y5 = x5 * r5 + (1 - r5) * np.random.rand(n5)
plt.plot(x5, y5)
plt.grid(True)

a5 = (np.sum(x5) * np.sum(y5) - n5 * np.sum(x5 * y5)) / (np.sum(x5) * np.sum(x5) - n5 * np.sum(x5 * x5))
b5 = (np.sum(y5) - a5 * np.sum(x5)) / n5

R5 = (np.sum(x5) - np.mean(x5) * (np.sum(y5) - np.mean(y5)))/np.sqrt(
    (np.sum(x5) - np.mean(x5)) ** 2 * (np.sum(y5) - np.mean(y5)) ** 2)

print(R5)
print(a5, b5)
