import matplotlib.pyplot as plt
import numpy
import math

# 1.2 задание длина вектора
A = int(input("Введите начальную координату: "))
B = int(input("Введите конечную координату: "))

print("Длина вектора равна: {}".format(B - A))

# 3.1 задание окружность (все в одном графике)

dots = 3600
x = []
x1 = []
y = []
y1 = []
R = float(input("Введите радиус: "))
for i in range(dots):
    y_ = i * (R / dots)
    x_ = math.sqrt(math.fabs(math.pow(R, 2) - math.pow(y_, 2)))
    x.append(x_)
    y.append(y_)
    x1.append(-x_)
    y1.append(-y_)

plt.plot(x, y1)
plt.plot(x1, y)
plt.plot(x, y)
plt.plot(x1, y1)


# 3.2 задание эллипс
ex = []
ey = []
ex1 = []
ey1 = []
a = float(input("Введите a: "))
b = float(input("Введите b: "))

for i in range(dots):
    ex_ = i * a / dots
    ey_ = math.sqrt((1 - math.pow(ex_, 2)/math.pow(a, 2))*math.pow(b, 2))
    ex.append(ex_)
    ey.append(ey_)
    ex1.append(-ex_)
    ey1.append(-ey_)

print(ex)
plt.plot(ex, ey)
plt.plot(ex1, ey)
plt.plot(ex, ey1)
plt.plot(ex1, ey1)


# 3.3 задание гипербола

xg = []
yg = []
xg1 = []
yg1 = []
c = float(input("Введите c: "))
d = float(input("Введите d: "))

for i in range(dots):
    yg_ = i * d / dots
    xg_ = math.sqrt((math.pow(yg_ / d, 2) + 1) * math.pow(c, 2))
    xg.append(xg_)
    yg.append(yg_)
    xg1.append(-xg_)
    yg1.append(-yg_)

print(xg)
print(yg)
plt.plot(xg, yg)
plt.plot(xg, yg1)
plt.plot(xg1, yg1)
plt.plot(xg1, yg)

plt.show(block=True)


